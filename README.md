---
# __bkc__


simple corporate site


### __Content__

1. <em id="c1">[Used technologies](#s1)</em>
2. <em id="c2">[Futures](#s2)</em>
3. <em id="c3">[Page tree](#s3)</em>
4. <em id="c4">[Page descriptions](#s4)</em>
5. <em id="c5">[BD structure](#s5)</em>


---
<h3 id="s1">Used technologies:</h>[↩](#c1)

- Python
- Django
- HTML5
- CSS3
- Grid
- JS


---
<h3 id="s2">Futures:</h>[↩](#c2)

- Main page with animation
- Static pages of solutions and services
- Contacts page with feedback form, contact information, map
- Static news pages
- Header with logo and contacts
- Top nawbar
- Side menu
- Language switcher (Ua, En, Ru)
- Video catalog
- Image catalog
- "Go to top" buttons
- Social keys (Facebook, Youtube)
- Image carousel
- Responsive design
- Editor for news pages
- https
- Products: description, characteristics, materials (docs, image, video), contact me
- Bread crumbs
- Footer with "Folow us" and "Subscribe" buttons
- Search
- Crosslinks with main site


---
<h3 id="s3">Page tree:</h>[↩](#c3)

		Main
		|
		|---Solutions
		|	\---Solution #1 ... Solution #N
		|---Services
		|	\---Service #1 ... Service #N
		|---News
		|	\---News #1 ... News #N
		|---Portfolio
		|	\---Project #1 ... Project #N
		|---About
		|	|---Resourses
		|	|---Clients
		|	|---Partners
		|	|---Certificates
		|	\---Career
		|		\---Vacancy #1 ... Vacancy #N
		|---Contacts
		|---Search
		|---Site map
		|---Page 404
		|
		\---Admin pages (default)


---
<h3 id="s4">Page descriptions:</h>[↩](#c4)

| # | Page | Functionality | Body <sup id="a1">[1](#f1)</sup> | Sections <sup id="a2">[2](#f2)</sup> |
| --- | --- | --- | --- | --- |
| 1 | Main | Entering point | A(L)(N(TBIL)) | HNSAF |
| 2 | Solutions | List of solutions | (TBIL) | HNSAF |
| 3 | Solution #N |  | TDHRF | HNSAF |
| 4 | Products |  | (TBIL) | HNSAF |
| 5 | Product #N |  | TDHRF | HNSAF |
| 6 | Services |  | (TBIL) | HNSAF |
| 7 | Service #N |  | TDRF | HNSAF |
| 8 | News |  | (TBIL) | HNSAF |
| 9 | New #N |  | TD | HNSAF |
| 10 | Portfolio |  | (TBIL) | HNSAF |
| 11 | Project #N |  | TD | HNSAF |
| 12 | About |  | TD(L) | HNSAF |
| 13 | Resourses |  | TD | HNSAF |
| 14 | Clients |  | (TBIL) | HNSAF |
| 15 | Partners |  | (TBIL) | HNSAF |
| 16 | Certificates |  | (TI) | HNSAF |
| 17 | Career |  | D(TBL) | HNSAF |
| 18 | Vacancy #N |  | TDF | HNSAF |
| 19 | Contacts |  | TCMFL | HNSAF |
| 20 | Search |  | T(TBL) | HNSAF |
| 21 | Site map |  | (TL) | HNSAF |
| 22 | Page 404 |  | DL | HNSAF |


<b id="f1">1</b> Body_elements:[↩](#a1)

- A - Animated image with responsive links
- () - List of ...
- T - Title
- B - Brief
- I - Image
- N - Short news (title, Brief and Image of News)
- D - Description (text, tables, images, videos)
- H - Technical characteristic
- R - Useful resources (datasheets, presentations, manuals, videos etc.)
- F - Feedback form
- L - Link
- M - Map
- C - Contacts

<b id="f2">2</b> Sections:[↩](#a2)

- H - Header,
- N - Navbar,
- B - Bread crumbs,
- S - Sidebar,
- A - Aside,
- F - Footer,
- U - "Go to top" button


---
<h3 id="s5">BD structure:</h>[↩](#c5)

| Type |
| --- |
| id |
| title |

| Upload |
| --- |
| id |
| type_id |
| title |
| slug |
| data |

| Class |
| --- |
| id |
| title |

| Company |
| --- |
| id |
| class_id |
| title |
| upload_id |
| brief |
| url |

| Category |
| --- |
| id |
| title |

| Post |
| --- |
| id |
| category_id |
| title |
| brief |
| upload_id |
| description |
| characteristic |
| resources |
