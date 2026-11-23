=====================================================================
USED LAPTOPS DATASET (NIGERIA) - DATA DOCUMENTATION
=====================================================================

1. OVERVIEW
---------------------------------------------------------------------
This document explains the sources, column definitions, limitations
and currency used in the accompanying CSV file of used laptop
listings. The dataset covers the brands HP, Dell, Lenovo, Apple,
ASUS, Acer, MSI and Toshiba. Each row represents one laptop listing
(or one laptop model/configuration) with its specifications and its
asking price in Nigerian naira.


2. DATA SOURCES
---------------------------------------------------------------------
Listings were collected from three online marketplaces:

  1. Jiji Nigeria
     https://jiji.ng/computers-and-laptops
     A large classifieds marketplace where individuals and shops
     post used and new laptops. Prices are set by the sellers.

  2. Reusers
     https://reusers.com/buy/categories/laptops
     A marketplace focused on refurbished and second-hand
     electronics, including laptops.

  3. 3jlisting
     https://www.3jlisting.com/listings
     An online listings platform where sellers advertise laptops
     and other items.

All prices and specifications are as advertised on these platforms.
They have not been independently verified.


3. COLUMN EXPLANATIONS (ALL 20 DATASET FIELDS)
---------------------------------------------------------------------
NOTE: If your CSV header names differ slightly from the names below,
treat these as the descriptions of the equivalent columns.

 1. Listing_ID        - Unique row number used to identify each
                        entry in the dataset.
 2. Brand             - Manufacturer of the laptop (HP, Dell,
                        Lenovo, Apple, ASUS, Acer, MSI, Toshiba).
 3. Model             - Specific model name or number as shown in
                        the listing (e.g. EliteBook 840 G5).
 4. Series            - Product family or line the model belongs to
                        (e.g. EliteBook, ThinkPad, MacBook Pro).
 5. Processor         - CPU name and tier (e.g. Intel Core i5,
                        AMD Ryzen 5, Apple M1).
 6. CPU_Generation    - Generation or release class of the
                        processor (e.g. 8th Gen).
 7. RAM_GB            - Installed memory in gigabytes.
 8. Storage_GB        - Total storage capacity in gigabytes
                        (1 TB recorded as 1000 GB).
 9. Storage_Type      - Type of storage drive: SSD or HDD (or a
                        combination of both).
10. Condition         - State of the laptop as described by the
                        seller (e.g. Foreign Used / Tokunbo,
                        Nigerian Used, Refurbished).
11. Price_NGN         - Asking price in Nigerian naira (see
                        section 5).
12. Source            - Marketplace the listing came from (Jiji
                        Nigeria, Reusers or 3jlisting).


4. LIMITATIONS
---------------------------------------------------------------------
Please keep the following in mind when using this dataset:

 a) Outdated listings
    Marketplace ads are often left up after the item has sold or
    the price has changed. Some rows may describe laptops that are
    no longer available at the stated price. Think of it like a
    street-market chalkboard that nobody wipes clean.

 b) Negotiable prices
    Prices on Nigerian marketplaces are asking prices, not final
    sale prices. Buyers commonly negotiate, so actual transaction
    prices are often lower than the listed figures.

 c) Data reliability
    Listings are created by individual sellers and shops with no
    guaranteed quality control. Typos, duplicated ads, exaggerated
    descriptions and mislabelled specs are possible. The dataset
    reflects what was advertised, not what was verified.

 d) Snapshot in time
    Laptop prices in Nigeria move with demand, supply and the
    exchange rate. The data represents a single collection period
    and may not reflect current prices.


5. CURRENCY
---------------------------------------------------------------------
All prices are in Nigerian naira (NGN / the naira symbol). No
foreign-exchange conversion has been applied. Prices were NOT
converted from or to US dollars or any other currency. If you
compare this data with dollar-priced sources, convert using the
exchange rate for the relevant date.


6. SUGGESTED USE
---------------------------------------------------------------------
This dataset is suited to rough price comparisons between brands and
specifications, exploratory analysis and learning exercises. It is
not suited to precise valuation or as proof of what any laptop
actually sold for.

=====================================================================
END OF DOCUMENT
=====================================================================
