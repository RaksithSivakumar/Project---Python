import phonenumbers
from phonenumbers import geocoder, carrier, timezone

phone_number = "+9112345670"  

parsed_number = phonenumbers.parse(phone_number)

location = geocoder.description_for_number(parsed_number, "en")

service_provider = carrier.name_for_number(parsed_number, "en")

timezones = timezone.time_zones_for_number(parsed_number)

is_valid = phonenumbers.is_valid_number(parsed_number)

print(f"Phone Number: {phone_number}")
print(f"Location: {location}")
print(f"Service Provider: {service_provider}")
print(f"Time Zones: {timezones}")
print(f"Valid Number: {is_valid}")
