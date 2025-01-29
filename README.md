# EBAYZ - Amazon Clone E-Commerce Website

## Overview
EBAYZ is a simplified e-commerce platform designed to replicate key functionalities of Amazon. It allows users to browse products, add items to their cart, make purchases, and manage their accounts. Sellers can list products, manage orders, and update product details, while administrators have control over the platform. The project emphasizes ease of deployment, low complexity, and minimal maintenance, making it ideal for self-hosting users.

## Features
- **User Module**: Users can register, browse products, add to cart, checkout, and update account settings.
- **Seller Module**: Sellers can add, update, and manage their product listings.
- **Admin Dashboard**: Administrators can manage users, sellers, and products.
- **Secure Authentication**: Login and registration with email/phone number and password.
- **Product Management**: View product details, reviews, and add to cart functionality.
- **Shopping Cart & Checkout**: Users can manage their cart and place orders with address input.

## Technologies Used
- **Frontend**: Django (Python Web Framework), HTML, CSS, JavaScript
- **Backend**: Django (Python)
- **Database**: SQLite
- **Development Methodology**: Waterfall Model

## System Design
- **Homepage**: Displays featured products, categories, and search functionality.
- **Product Page**: Shows detailed product information and reviews.
- **Cart & Checkout**: Allows users to add items, review their cart, and complete purchases.
- **Seller Dashboard**: Enables sellers to manage their inventory and orders.
- **Admin Panel**: Provides full control over website operations.

## Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ebayz.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ebayz
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the server:
   ```bash
   python manage.py runserver
   ```
6. Access the website at `http://127.0.0.1:8000/`

## Conclusion
EBAYZ is a simple, efficient e-commerce solution designed for easy deployment and management. It provides essential e-commerce functionalities with a focus on low complexity, making it a great choice for small businesses and independent sellers.


