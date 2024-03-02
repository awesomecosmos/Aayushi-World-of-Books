library(googlesheets4)

my_sheet_url <- read.csv("secrets/link_to_my_sheet.csv")$link_to_my_sheet

sheet <- gs4_get(
  my_sheet_url
)

sheet_data <- read_sheet(sheet)