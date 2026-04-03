# All reusable UI components are located in  /components/ui/

1. Badge

File: Badge.jsx

Small label component used to display status or counts.

Props:

* text

Usage:

* Table status  
* Labels  
* Counters

2. Button

File: Button.jsx

Reusable button with multiple variants.

Props:

* variant (primary | success | warning | danger)  
* onClick  
* children

Usage:

* Actions  
* Forms  
* Modals

3. Card

File: Card.jsx

Dashboard summary card component.

Props:

* title  
* color (Tailwind background class)  
* children

Usage:

* Dashboard metric cards  
* Summary sections

4. ChartCard

File: ChartCard.jsx

Wrapper component for charts with header and body layout.

Props:

* title  
* children

Usage:

* Area chart container  
* Bar chart container

5. InputNav

File: InputNav.jsx

Styled input component used specifically in the Navbar.

Props:

* placeholder

Usage:

* Navbar search input

6. Modal

File: Modal.jsx

Basic modal overlay component.

Props:

* isOpen  
* children

Usage:

* Dialogs  
* Confirm actions

7. Navbar (Dashboard)

File: Navbar.jsx

Top navigation bar for dashboard pages.

Features:

* Sidebar toggle (hamburger)  
* Search input  
* Notification icon  
* Profile navigation  
* Home navigation

Used in:

* /dashboard layout

8. PublicNavbar

File: PublicNavbar.jsx

Simple navigation bar for public pages.

Features:

* Logo  
* Navigation tabs (Home, About, Dashboard)

Used in:

* Landing page  
* About page

9. Sidebar

File: Sidebar.jsx

Dashboard sidebar navigation.

Features:

* Toggleable sidebar  
* Navigation links  
* Dashboard sections

Used in:

* /dashboard layout  
    
10. TableCard

File: TableCard.jsx

Wrapper component for tables with header and content area.

Props:

* title  
* children

Usage:

* Data tables  
* Dashboard listings

End of UI Component Documentation