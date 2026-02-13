# Django Games Catalog

This project is a **Django web application** developed as a group assignment using **Django, HTML, and CSS**.  
The website is designed as a **games catalog**, where users can browse games and view detailed information for each one.

## 📌 Project Features

- A page that displays each game with:
  - **Title**
  - **Publisher**
  - **Developer**
  - **Category**
  - **Description**
- Each game page includes **cross-links**:
  - Clicking on the **publisher** redirects to the Publisher detail page
  - Clicking on the **developer** redirects to the Developer detail page
- Pages are styled using **custom CSS** for a consistent and clean layout.

## Models & Relationships

The project includes multiple Django models with relationships, such as:
- **Game**
- **Publisher**
- **Developer**
- **Category**

Games are connected to their publisher, developer, and category through Django relationships, allowing navigation between related objects.

## Technologies Used

- **Django** (backend, routing, models, templates)
- **HTML** (Django templates)
- **CSS** (styling)

## Learning Outcomes

This project demonstrates:
- Building a multi-page Django application
- Working with **related models**
- Rendering dynamic content using templates
- Creating cross-linked detail pages
- Styling a web application with CSS
