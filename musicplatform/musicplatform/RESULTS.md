- Create Some Artists

artist1 = Artist(stagename='Kanye' , social_link = "https://www.instagram.com/kanye")
artist1.save()

artist2=Artist(stagename="Eminem", social_link = "https://www.instagram.com/eminem")
artist2.save()

artist3 = Artist(stagename="The Weeknd", social_link="https://www.instagram.com/theweeknd")
artist3.save()

artist4= Artist.objects.create(stagename="Abyusif",social_link="https://www.instagram.com/abyusif")
artist4.save()

artist5 = Artist.objects.create(stagename="illiam",social_link="https://www.instagram.com/illiam")  
artist5.save()

artist6=Artist.objects.create(stagename="thesynaptic",social_link="https://www.instagram.com/thesynaptic")
artist6.save()

aritst8 = Artist(stagename="test8",social_link="https://www.instagram.com/test8")
aritst9 = Artist(stagename="test9",social_link="https://www.instagram.com/test9")  
aritst8.save()
aritst9.save()
================================================================================================================

- list down all artists
  Artist.objects.all()
  <QuerySet [<Artist: Kanye>, <Artist: Eminem>, <Artist: The Weeknd>, <Artist: Abyusif>, <Artist: illiam>, <Artist: thesynaptic>, <Artist: test7>, <Artist: test8>, <Artist:
  test9>]>

================================================================================================================

- list down all artists sorted by name

Artist.objects.order_by('stagename')
<QuerySet [<Artist: Abyusif>, <Artist: Eminem>, <Artist: Kanye>, <Artist: The Weeknd>, <Artist: illiam>, <Artist: test7>, <Artist: test8>, <Artist: test9>, <Artist: thesynaptic>]>

================================================================================================================

- list down all artists whose name starts with 'a'

Artist.objects.filter(stagename\_\_startswith='a')
<QuerySet [<Artist: Abyusif>]>

================================================================================================================

- in 2 different ways, create some albums and assign them to any artists

album1 = Album(name="Kanye Album", release_datetime=timezone.now(), creation_datetime=timezone.now(), cost=100.66, artist=artist1)
album1.save()

album2 = Album(name="YFGYY", release_datetime=timezone.now(), creation_datetime=timezone.now(), cost=999.99, artist=artist2)
album2.save()

album3 = Album(name="OM Al Mawjat", release_datetime=timezone.now(), creation_datetime=timezone.now(), cost=240.9, artist=artist3)
album3.save()

Album.objects.create(name="Before Bed", release_datetime=timezone.now(), creation_datetime=timezone.now(), cost=500.85, artist=artist4)  
<Album: Before Bed>

================================================================================================================

- get the latest released album

latest_album = Album.objects.latest('release_datetime')
print(latest_album)
Before Bed

================================================================================================================

- get the latest released album for a specific artist

latest_album = Album.objects.filter(artist=var_artist).latest('release_datetime')

================================================================================================================

- get all albums released before today

albums = Album.objects.filter(release_datetime\_\_lt=timezone.now().date())
print(albums)
<QuerySet []>

================================================================================================================

- get all albums released today or before but not after today

albums = Album.objects.filter(release_datetime\_\_lte=timezone.now().date())  
<QuerySet []>

================================================================================================================

- count the total number of albums

Album.objects.count()  
5

================================================================================================================

- in 2 different ways, for each artist, list down all of his/her albums
  = First Way Using The Objects Manager:
  artists_list= Artist.objects.all()
  for artist in artists_list :
  artist.stagename
  artist.albums.all()
  Output ->
  'Kanye'
  <QuerySet [<Album: Kanye Album>, <Album: Kanye Album>]>
  'Eminem'
  <QuerySet []>
  'The Weeknd'
  <QuerySet []>
  'Abyusif'
  <QuerySet [<Album: YFGYY>]>
  'illiam'
  <QuerySet [<Album: Before Bed>]>
  'thesynaptic'
  <QuerySet [<Album: OM Al Mawjat>]>
  'test7'
  <QuerySet []>
  'test8'
  <QuerySet []>
  'test9'
  <QuerySet []>

= The Second Way Using the related object reference:

for album in Album.objects.select_related('artist').all():
... album.artist.stagename
... album.name
...
'Kanye'
'Kanye Album'
'Abyusif'
'YFGYY'
'thesynaptic'
'OM Al Mawjat'
'illiam'
'Before Bed'
'Kanye'
'Kanye Album'

================================================================================================================

- list down all albums ordered by cost then by name (cost has the higher priority)

Album.objects.all().order_by('cost','name')  
<QuerySet [<Album: Kanye Album>, <Album: Kanye Album>, <Album: OM Al Mawjat>, <Album: Before Bed>, <Album: YFGYY>]>

================================================================================================================

- We can do the following Query

Artist.objects.all().order_by("approved_albums")
