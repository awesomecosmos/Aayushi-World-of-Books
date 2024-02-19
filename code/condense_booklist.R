library(tidyverse)
library(readxl)

goodreads_library_export_csv <- read.csv("data/goodreads_library_export.csv")
goodreads_library_export_xlsx <- read_excel("data/goodreads_library_export.xlsx")
libby <- read.csv("data/libbytimeline-activities.csv")
office_books <- read_excel("data/office_books.xlsx")
simplified_booklist_csv <- read.csv("data/simplified_book_list.csv")
simplified_booklist_xlsx <- read_excel("data/simplified_book_list.xlsx")

goodreads_library_export_csv_new <- goodreads_library_export_csv %>%
  mutate(
    `ISBN` = na_if(`ISBN`, ""),
    `Additional.Authors` = na_if(`Additional.Authors`, ""),
    `Date.Read` = na_if(`Date.Read`, "")
  ) %>% 
  rename(
    "Author l-f" = "Author.l.f",
    "Additional Authors" = "Additional.Authors",
    "ISBN10" = "ISBN",
    "Number of Pages" = "Number.of.Pages",
    "Year Published" = "Year.Published",
    "Original Publication Year" = "Original.Publication.Year",
    "Date Read" = "Date.Read",
    "Date Added" = "Date.Added"
  ) %>%
  select(
    "Title", "Author", "Author l-f", "Additional Authors",
    "ISBN10", "ISBN13", "Number of Pages", "Year Published",
    "Original Publication Year", "Date Read"
  ) %>% 
  mutate(
    `ISBN10` = as.character(`ISBN10`),
    `ISBN13` = as.character(`ISBN13`)
  ) %>% 
  # mutate(
  #   ISBN10 = ifelse(!is.na(ISBN10), format(as.character(ISBN10), scientific = FALSE), NA),
  #   ISBN13 = ifelse(!is.na(ISBN13), format(as.character(ISBN13), scientific = FALSE), NA)
  # ) %>%
  distinct()

goodreads_library_export_xlsx_new <- goodreads_library_export_xlsx %>%
  rename("ISBN10" = "ISBN") %>%
  select(
    "Title", "Author", "Author l-f", "Additional Authors",
    "ISBN10", "ISBN13", "Number of Pages", "Year Published",
    "Original Publication Year", "Date Read"
  ) %>% 
  mutate(
    `ISBN10` = as.character(`ISBN10`),
    `ISBN13` = as.character(`ISBN13`)
  ) %>% 
  # mutate(
  #   `ISBN10` = ifelse(!is.na(`ISBN10`), format(as.numeric(`ISBN10`), scientific = FALSE), NA),
  #   `ISBN13` = ifelse(!is.na(`ISBN13`), format(as.numeric(`ISBN13`), scientific = FALSE), NA)
  # ) %>%
  distinct()

condense_goodreads <- rbind(
  goodreads_library_export_csv_new,
  goodreads_library_export_xlsx_new
) %>%
  mutate(
    `ISBN10` = as.character(`ISBN10`),
    `ISBN13` = as.character(`ISBN13`)
  ) %>% 
  distinct()

libby_new <- libby %>%
  select(title, author, isbn, timestamp) %>%
  mutate(
    # isbn = ifelse(!is.na(isbn), format(as.numeric(isbn), scientific = FALSE), NA),
    isbn = as.character(isbn),
    author = ifelse(!is.na(author),
      sapply(
        strsplit(as.character(author), " "),
        function(x) paste(rev(x), collapse = ", ")
      ),
      NA
    ),
    timestamp = ifelse(!is.na(timestamp),
      format(as.Date(timestamp, "%B %d, %Y %H:%M"), "%m/%d/%Y"),
      NA
    )
  ) %>%
  rename(
    "Title" = "title", "ISBN13" = "isbn",
    "Author l-f" = "author", "Date Borrowed" = "timestamp"
  ) %>%
  mutate(
    "Year Read" = as.numeric(substr(`Date Borrowed`, nchar(`Date Borrowed`) - 3, nchar(`Date Borrowed`)))
  ) %>%
  mutate(
  #   `ISBN10` = as.character(`ISBN10`),
  `ISBN13` = as.character(`ISBN13`)
  ) %>%
  distinct()


office_books_new <- office_books %>%
  rename("Title" = "Book Title", "ISBN13" = "ISBN-13", "ISBN10" = "ISBN-10") %>%
  # mutate(
  #   `ISBN10` = ifelse(!is.na(`ISBN10`), format(as.numeric(`ISBN10`), scientific = FALSE), NA),
  #   `ISBN13` = ifelse(!is.na(`ISBN13`), format(as.numeric(`ISBN13`), scientific = FALSE), NA)
  # ) %>%
  mutate(
    `ISBN10` = as.character(`ISBN10`),
    `ISBN13` = as.character(`ISBN13`)
  ) %>% 
  distinct()

simplified_booklist_csv_new <- simplified_booklist_csv %>%
  rename(
    "Title" = "Book.Title", "Author l-f" = "Author.l.f",
    "Additional Authors" = "Additional.Authors",
    "ISBN10" = "ISBN.10", "ISBN13" = "ISBN.13",
    "Number of Pages" = "Number.of.Pages",
    "Year Published" = "Year.Published",
    "Original Publication Year" = "Original.Publication.Year",
    "Year Read" = "Year.Read",
    "User Genre" = "User.Genre",
    "Fiction Status" = "Fiction.Status",
    "User Tags" = "User.Tags",
    "Ownership Status" = "Ownership.Status",
    "Buy?" = "Buy."
  ) %>%
  # mutate(
  #   `ISBN10` = ifelse(!is.na(`ISBN10`), format(as.numeric(`ISBN10`), scientific = FALSE), NA),
  #   `ISBN13` = ifelse(!is.na(`ISBN13`), format(as.numeric(`ISBN13`), scientific = FALSE), NA)
  # ) %>%
  mutate(
    `ISBN10` = as.character(`ISBN10`),
    `ISBN13` = as.character(`ISBN13`)
  ) %>% 
  distinct()

simplified_booklist_xlsx_new <- simplified_booklist_xlsx %>%
  rename("Title" = "Book Title", "ISBN10" = "ISBN-10", "ISBN13" = "ISBN-13") %>%
  # mutate(
  #   `ISBN10` = ifelse(!is.na(`ISBN10`), format(as.numeric(`ISBN10`), scientific = FALSE), NA),
  #   `ISBN13` = ifelse(!is.na(`ISBN13`), format(as.numeric(`ISBN13`), scientific = FALSE), NA)
  # ) %>%
  mutate(
    `ISBN10` = as.character(`ISBN10`),
    `ISBN13` = as.character(`ISBN13`)
  ) %>% 
  distinct()

condense_simplified_booklist <- rbind(
  simplified_booklist_csv_new,
  simplified_booklist_xlsx_new
) %>%
  mutate(
    `ISBN10` = as.character(`ISBN10`),
    `ISBN13` = as.character(`ISBN13`)
  ) %>% 
  distinct()
# condense_goodreads
# libby_new
# office_books_new
# condense_simplified_booklist

all_column_names <- unique(
  c(
    colnames(condense_goodreads), colnames(libby_new),
    colnames(office_books_new), colnames(condense_simplified_booklist)
  )
)

combined_data <- bind_rows(
  bind_cols(
    condense_goodreads,
    tibble::tibble(
      `Date Borrowed` = NA, `Year Read` = NA, `User Genre` = NA,
      `Fiction Status` = NA, `User Tags` = NA, `Ownership Status` = NA,
      `Buy?` = NA
    )
  ),
  bind_cols(
    libby_new,
    tibble::tibble(
      `Author` = NA, `Additional Authors` = NA, `ISBN10` = NA,
      `Number of Pages` = NA, `Year Published` = NA,
      `Original Publication Year` = NA, `Date Read` = NA, `User Genre` = NA,
      `Fiction Status` = NA, `User Tags` = NA, `Ownership Status` = NA,
      `Buy?` = NA
    )
  ),
  bind_cols(
    office_books_new,
    tibble::tibble(
      `Author` = NA, `Additional Authors` = NA,
      `Number of Pages` = NA, `Year Published` = NA,
      `Original Publication Year` = NA, `Date Read` = NA, `Date Borrowed` = NA
    )
  ),
  bind_cols(
    condense_simplified_booklist,
    tibble::tibble(
      `Author` = NA, `Date Read` = NA, `Date Borrowed` = NA
    )
  )
) %>%
  distinct()
