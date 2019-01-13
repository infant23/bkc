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
| 4 | Services |  | (TBIL) | HNSAF |
| 5 | Service #N |  | TDRF | HNSAF |
| 6 | News |  | (TBIL) | HNSAF |
| 7 | New #N |  | TD | HNSAF |
| 8 | Portfolio |  | (TBIL) | HNSAF |
| 9 | Project #N |  | TD | HNSAF |
| 10 | About |  | TD(L) | HNSAF |
| 11 | Resourses |  | TD | HNSAF |
| 12 | Clients |  | (TBIL) | HNSAF |
| 13 | Partners |  | (TBIL) | HNSAF |
| 14 | Certificates |  | (TI) | HNSAF |
| 15 | Career |  | D(TBL) | HNSAF |
| 16 | Vacancy #N |  | TDF | HNSAF |
| 17 | Contacts |  | TCMFL | HNSAF |
| 18 | Search |  | T(TBL) | HNSAF |
| 19 | Site map |  | (TL) | HNSAF |
| 20 | Page 404 |  | DL | HNSAF |


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
| uploads_id |
