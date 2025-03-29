from smartphone import Smartphone

catalog = [
    Smartphone("iPhon1", "one", "+79104582578"),
    Smartphone("iPhon2", "two", "+79204582578"),
    Smartphone("iPhon3", "three", "+79514582578"),
    Smartphone("iPhon4", "four", "+79614582578"),
    Smartphone("iPhon5", "five", "+79104582578")
]

for smart in catalog:
    print(f"{smart.marka} - {smart.model}. {smart.number}")
