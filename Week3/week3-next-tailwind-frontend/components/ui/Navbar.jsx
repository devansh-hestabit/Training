"use client";
import Input from "@/components/ui/InputNav";

export default function Navbar({ isOpen, onToggleSidebar }) {
  return (
    <header className="h-16 bg-gray-800 text-white flex items-center justify-between px-6">
      {/* Left side */}
      <div className="flex items-center gap-4">
        <span className="text-lg font-semibold">HestaCart</span>

        <button
          onClick={onToggleSidebar}
          className={`
            text-xl cursor-pointer
            transition-transform duration-300
            ${isOpen ? "rotate-90" : "rotate-0"}
          `}
        >
          ☰
        </button>
      </div>

      {/* Right side */}
      <div className="flex items-center gap-4">
        <div className="relative">
          <span className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-500">
            🔍
          </span>

          <Input placeholder="Search for..." />
        </div>

        <span className="cursor-pointer">🔔</span>
        <span className="cursor-pointer">👤</span>
      </div>
    </header>
  );
}
