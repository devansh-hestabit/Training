## Project Overview

**HestaCart** is a fully responsive, multi-page frontend dashboard application built using **Next.js (App Router)** and **Tailwind CSS**, without any backend integration.

The project simulates a real-world **SaaS admin dashboard**, including public pages, authentication UI, dashboard analytics, user management, and profile management.

This project was developed as a **capstone mini-project** covering concepts from **Day 1 to Day 5** of the training program.

## Project Structure

```
week3-next-tailwind-frontend
    ├── .gitignore
    ├── README.md
    ├── UI-COMPONENT-DOCS.md
    ├── screenshots
    │   ├── landing-page.png
    │   ├── about-page.png
    │   ├── login-page.png
    │   ├── profile-page.png
    │   ├── users-page.png
    │   └── dashboard-page.png
    ├── app
    │   ├── (public)
    │   │   ├── about
    │   │   │   └── page.jsx
    │   │   ├── login
    │   │   │   └── page.jsx
    │   │   ├── layout.jsx
    │   │   └── page.jsx
    │   ├── dashboard
    │   │   ├── layout.jsx
    │   │   ├── page.jsx
    │   │   ├── users
    │   │   │   └── page.jsx
    │   │   └── profile
    │   │       └── page.jsx
    │   ├── favicon.ico
    │   ├── globals.css
    │   └── layout.jsx
    ├── components
    │   ├── charts
    │   │   ├── AreaChart.jsx
    │   │   └── BarChart.jsx
    │   ├── landing
    │   │   ├── Features.jsx
    │   │   ├── Footer.jsx
    │   │   ├── Hero.jsx
    │   │   └── Testimonials.jsx
    │   ├── tables
    │   │   ├── UsersTable.jsx
    │   │   └── DataTable.jsx
    │   └── ui
    │       ├── Badge.jsx
    │       ├── Button.jsx
    │       ├── Card.jsx
    │       ├── ChartCard.jsx
    │       ├── InputNav.jsx
    │       ├── Modal.jsx
    │       ├── Navbar.jsx
    │       ├── PublicNavbar.jsx
    │       ├── Sidebar.jsx
    │       └── TableCard.jsx
    ├── eslint.config.mjs
    ├── jsconfig.json
    ├── next.config.mjs
    ├── package-lock.json
    ├── package.json
    ├── postcss.config.mjs
    └── public
        ├── hero.png
        └── profile.jpeg

```

## Reusable UI Components

All reusable UI components are located in:

### components/ui

### Components Used

- Button
- InputNav
- Modal
- Card
- ChartCard
- TableCard
- Badge
- Navbar
- PublicNavbar
- Sidebar
- UsersTable

## Pages Implemented

### Public Pages

- `/` – Landing Page
- `/about` – About Page
- `/login` – Login Page (static modal UI)

### Dashboard Pages

- `/dashboard` – Dashboard Overview
- `/dashboard/users` – Users Listing Table
- `/dashboard/profile` – Profile Page

## Screenshots

Screenshots for the following pages:

## 🖼️ Screenshots

### Homepage

![Homepage](week3-next-tailwind-frontend/screenshots/landing-page.png)

### Dashboard

![Dashboard](week3-next-tailwind-frontend/screenshots/dashboard-page.png)

### Users Page

![Users](week3-next-tailwind-frontend/screenshots/users-page.png)

### Profile Page

![Profile](week3-next-tailwind-frontend/screenshots/profile-page.png)

### Login Page

![Login](week3-next-tailwind-frontend/screenshots/login-page.png)

### About Page

![About](week3-next-tailwind-frontend/screenshots/about-page.png)

## Challenges Faced

- Understanding Next.js App Router (`page.jsx` vs `layout.jsx`)
- Handling nested layouts and avoiding duplicate navbars
- Confusion between Client Components and Server Components
- Managing sidebar and navbar layout alignment
- Making tables responsive on smaller screens
- Structuring components properly for reuse

## Key Learnings & Lessons

- How Next.js App Router works in real projects
- Difference between SSG, CSR, and Client Components
- Importance of reusable components
- Tailwind CSS utility-first workflow
- Responsive design using Flexbox and Grid
- Clean project and folder structure
- Image optimization using `next/image`
