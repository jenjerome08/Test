from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=50, null=True)
    description = models.TextField(blank=True)
    started_date = models.DateField(null=True)

    def __str__(self):
        return self.name
class Musician(models.Model):
    pen_name = models.CharField(max_length=50, null=True)
    full_name = models.CharField(max_length=50, null=True)
    age = models.IntegerField(null=True)
    phone = models.IntegerField(blank=True)
    email = models.EmailField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to='profile_picture/', blank=True)
    group = models.ManyToManyField(Group, related_name='musicians')

    def __str__(self):
        return self.pen_name
    
class Album(models.Model):
    musician = models.ForeignKey(Musician, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50, null=True)
    description = models.TextField(blank=True)
    photo_album = models.ImageField(upload_to='albums/', blank=True)
    release_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title

class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50, null=True)
    description = models.TextField(blank=True)
    release_date = models.DateField(auto_now=True)
    photo_track = models.ImageField(upload_to='tracks_photo/', blank=True)
    media_file = models.FileField(upload_to='tracks_audio/', blank=True)

    def __str__(self):
        return self.title

class Organizer(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name
class Contract(models.Model):
    organizer = models.ForeignKey(Organizer, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    terms = models.TextField(blank=True)
    payment = models.PositiveIntegerField(null=True)
    album = models.OneToOneField(Album, on_delete=models.CASCADE)
    def __str__(self):
        return f"Contract for {self.album.musician.pen_name}"

class MusicianContractStatus(models.Model):
    musician = models.ForeignKey(Musician, on_delete=models.SET_NULL, null=True)
    contract = models.OneToOneField(Contract, on_delete=models.SET_NULL, null=True)
    STATUS = (
        ('A', 'Accepted'),
        ('P', 'Pending'),
        ('D', 'Denied'),
    )
    status = models.CharField(max_length=1, choices=STATUS)

    def __str__(self):
        return f"{self.musician.pen_name}'s Status for Contract {self.contract.album.title}"

