class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/garden_buddy_database'
    SECRET_KEY = '123456789000000000'
    PERSONAL_RPI_SERIAL_ID = '10000000edc20395' # change according to your own personal rpi serial
    TEMPERATURE_RANGE = 3
    BRIGHTNESS_RANGE = 0.3
    MOISTURE_RANGE = 50
    SALINITY_RANGE = 0.1
    PH_RANGE = 0.1
