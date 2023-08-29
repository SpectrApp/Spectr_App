import cianparser

data = cianparser.parse(
    deal_type="sale",
    accommodation_type="flat",
    location="Санкт-Петербург",
    rooms=(5),
  #  start_page=1,
   # end_page=2,
    is_saving_csv=True,
    is_latin=False,
    is_express_mode=False,
    is_by_homeowner=False,
)

print(data[0])