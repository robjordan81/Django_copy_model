from django.db import models
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.related import ForeignKey
from django.db.models.deletion import CASCADE
#from numpy.distutils.fcompiler import none

# Create your models here.

def nameFile(instance, filename):
    print ("saving file from upload")
    return 'images/{filename}'.format(filename=filename)
    #return '/'.join(['images', str(instance.name), filename])

class UploadImageTest(models.Model):
    #name = models.CharField(max_length=100,null=True,blank=True)
    file = models.ImageField(upload_to=nameFile, blank=True, null=True)

class User(models.Model):
    name = models.CharField(max_length=200)

        
class Project(models.Model):
    name_project = models.CharField(max_length=200)
    
class Revision (Project):
    rev = models.IntegerField(default=0)

    def duplicate(self):
            
        """
        Duplicate a model instance, making copies of all foreign keys pointing
        to it. This is an in-place method in the sense that the record the
        instance is pointing to will change once the method has run. The old
        record is still accessible but must be retrieved again from
        the database.
        """
        # I had a known set of related objects I wanted to carry over, so I
        # listed them explicitly rather than looping over obj._meta.fields
        fks_to_copy = list(self.data_set.all()) + list(self.dataextra_set.all())# + list(self.fkeys_b.all())
    
        # Now we can make the new record
        self.pk = None
        self.id = None
        self.project_ptr_id = None
        self.rev=1#changing to up rev needs to be automated
        # Make any changes you like to the new instance here, then
        self.save()
    
        foreign_keys = {}
        for fk in fks_to_copy:
            fk.pk = None
            # Likewise make any changes to the related model here
            # However, we avoid calling fk.save() here to prevent
            # hitting the database once per iteration of this loop
            x = fk.__class__.__name__
            
            match x:
                case "DataExtra":
                    fk.data.revision=self
                    fk.data.save()
                    fk.revision = self
                    fk.save()
                    #print (fk)
                    #print ("all dataextra" + str(DataExtra.objects.all()))
                
                case _:
                    fk.revision = self
                    fk.save()            
            
            
#            if fk.__class__.__name__ == "DataExtra":
#                fk.data.revision=self
#                fk.data.save()
#                fk.revision = self
#                fk.save()
#                print (fk)
#                print ("all dataextra" + str(DataExtra.objects.all()))
#           else:
#                fk.revision = self
#                fk.save()
            
   #         try:
   #             # Use fk.__class__ here to avoid hard-coding the class name
   #             foreign_keys[fk.__class__].append(fk)
   #         except KeyError:
   #             foreign_keys[fk.__class__] = [fk]
    
        # Now we can issue just two calls to bulk_create,
        # one for fkeys_a and one for fkeys_b
   #     for cls, list_of_fks in foreign_keys.items():
   #         cls.objects.bulk_create(list_of_fks)
    

class Data(models.Model):
    revision = models.ForeignKey(Revision,on_delete=CASCADE)
    name_data = models.CharField(max_length=200)
    data_item = models.IntegerField()
    def __str__(self):
        return  "revision: " + str(self.revision.rev) + ":" + str(self.name_data)


class DataExtra(models.Model):
    revision = models.ForeignKey(Revision,on_delete=CASCADE)
    data = models.ForeignKey(Data, on_delete=CASCADE)
    name_data_ex = models.CharField(max_length=200)
    data_item_ex = models.IntegerField()
    def __str__(self):
        return  "revision: " + str(self.revision.rev) + ":" + str(self.name_data_ex) + ":" + str(self.data)

class Dimension (models.Model):
    name = models.CharField(max_length=6)
    nominal = models.DecimalField(max_digits=6,decimal_places=2)

class DimensionCalc (models.Model):
    name = models.CharField(max_length=20)
    dimension = models.ForeignKey(Dimension,on_delete=CASCADE)
    def dim_calc (self):
        dim = self
        nominal = Dimension.objects.get(Dimension=dim)
        return float(nominal*2)

class Stack (models.Model):
    name = models.CharField(max_length=6)
    
class StackLine (models.Model):
    stack = models.ForeignKey(Stack,on_delete=CASCADE)
    dim = models.ForeignKey(Dimension,on_delete=CASCADE,blank=True,null=True)
    dim_cal = models.ForeignKey(DimensionCalc,on_delete=CASCADE,blank=True,null=True)



