class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/garden_buddy_database'
    SECRET_KEY = '123456789000000000'
    PERSONAL_RPI_SERIAL_ID = '12345678'
    TEMPERATURE_RANGE = 3
    BRIGHTNESS_RANGE = 0.3
    MOISTURE_RANGE = 10
    SALINITY_RANGE = 10
    PH_RANGE = 1.0
