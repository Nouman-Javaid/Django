from django.db import models
from django.conf import settings

# Create your models here.


class Property(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True, null=True,
    )

    longitude = models.IntegerField()
    latitude = models.IntegerField()
    '''
    landArea = models.PositiveIntegerField()
    beds = models.PositiveIntegerField()
    baths = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    view = models.PositiveIntegerField()
    drawingRoom = models.PositiveIntegerField()
    diningRoom = models.PositiveIntegerField()
    kitchens = models.PositiveIntegerField()
    yearAdded = models.DateTimeField(auto_now_add=True)
    builtInYear = models.DateField(auto_now=True)
    city = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    propertyType = models.CharField(max_length=255)
    parkingSpaces = models.PositiveIntegerField()
    doubleGlazedWindows = models.CharField(max_length=255)
    centralAirConditioning = models.CharField(max_length=255)
    centralHeating = models.CharField(max_length=255)
    flooring = models.CharField(max_length=255)
    electricityBackup = models.CharField(max_length=255)
    wasteDisposal = models.CharField(max_length=255)
    lobbyInBuilding = models.CharField(max_length=255)
    floor = models.CharField(max_length=255)
    floors = models.CharField(max_length=255)
    floorsInBuilding = models.CharField(max_length=255)
    elevators = models.CharField(max_length=255)
    serviceElevatorsInBuilding = models.CharField(max_length=255)
    otherMainFeatures = models.CharField(max_length=255)
    furnished = models.CharField(max_length=255)
    servantQuarters = models.CharField(max_length=255)
    studyRoom = models.CharField(max_length=255)
    prayerRoom = models.CharField(max_length=255)
    powderRoom = models.CharField(max_length=255)
    gym = models.CharField(max_length=255)
    storeRooms = models.CharField(max_length=255)
    steamRoom = models.CharField(max_length=255)
    loungeSittingRoom = models.CharField(max_length=255)
    laundryRoom = models.CharField(max_length=255)
    otherRooms = models.CharField(max_length=255)
    broadbandInternetAccess = models.CharField(max_length=255)
    satelliteCableTVReady = models.CharField(max_length=255)
    intercom = models.CharField(max_length=255)
    businessCenterMediaRoomInBuilding = models.CharField(max_length=255)
    conferenceRoomInBuilding = models.CharField(max_length=255)
    atmMachines = models.CharField(max_length=255)
    otherBusinessCommunicationFacilities = models.CharField(max_length=255)
    lawnGarden = models.CharField(max_length=255)
    swimmingPool = models.CharField(max_length=255)
    sauna = models.CharField(max_length=255)
    jacuzzi = models.CharField(max_length=255)
    otherHealthcareRecreationFacilities = models.CharField(max_length=255)
    nearbySchools = models.CharField(max_length=255)
    nearbyHospitals = models.CharField(max_length=255)
    nearbyShoppingMalls = models.CharField(max_length=255)
    nearbyRestaurants = models.CharField(max_length=255)
    distanceFromAirport = models.CharField(max_length=255)
    nearbyPublicTransportService = models.CharField(max_length=255)
    otherNearbyPlaces = models.CharField(max_length=255)
    maintenanceStaff = models.CharField(max_length=255)
    securityStaff = models.CharField(max_length=255)
    facilitiesForDisabled = models.CharField(max_length=255)
    laundryDryCleaningFacility = models.CharField(max_length=255)
    '''
    '''
    def __str__(self):
        """Return model as a string"""
        return self.basic_property
    '''


class PropertyImages(models.Model):
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name='Gallery',
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    image = models.ImageField(upload_to='images/', blank=False)
    description = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    '''
    def __str__(self):
        """Return model as a string"""
        return self.extended_features
    '''


'''
class ProfileFeedItems(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return model as a string"""
        return self.status_text



chat_id 
user_id 
line_text 
created_at 
'''



''' 
class BasicProperties(models.Model):
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='basic_property_of_a',
    )
    beds = models.IntegerField()
    baths = models.IntegerField()
    price = models.IntegerField()
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', blank=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return model as a string"""
        return self.address
'''