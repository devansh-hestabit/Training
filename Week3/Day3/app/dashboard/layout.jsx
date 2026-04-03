"use client";

import Navbar from "@/components/ui/Navbar";
import Sidebar from "@/components/ui/Sidebar";
import { useState } from "react";

export default function DashboardLayout({ children }) {
  const [sidebarOpen, setSidebarOpen] = useState(false);

  return (
    <div>
      <Navbar
        isOpen={sidebarOpen}
        onToggleSidebar={() => setSidebarOpen(!sidebarOpen)}
      />

      <div className="flex">
        <Sidebar isOpen={sidebarOpen} />

        <main className="flex-1 p-6 bg-gray-100 min-h-screen">
          {children}
        </main>
      </div>
    </div>
  );
}
