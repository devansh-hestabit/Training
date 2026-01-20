"use client";
import Navbar from "@/components/ui/Navbar";
import "./globals.css";
import { useState } from "react";
import Sidebar from "@/components/ui/Sidebar";

export default function RootLayout({ children }) {
  const [sidebarOpen, setSidebarOpen] = useState(false);
  return (
    <html lang="en">
      <body>
        <Navbar
          isOpen={sidebarOpen}
          onToggleSidebar={() => setSidebarOpen(!sidebarOpen)}
        />

        <div className="flex">
          <Sidebar isOpen={sidebarOpen} />
          <main className="flex-1 p-6 bg-gray-50 min-h-screen">{children}</main>
        </div>
      </body>
    </html>
  );
}
