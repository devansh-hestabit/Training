export default function Navbar() {
  return (
    <header className="h-16 bg-gray-800 text-white flex items-center justify-between px-6">
      {/* Left side: Title + menu icon */}
      <div className="flex items-center gap-4">
        <span className="text-lg font-semibold">Start Bootstrap</span>

        <span className="text-xl cursor-pointer">☰</span>
      </div>

      {/* Right side: Search + icons */}
      <div className="flex items-center gap-4">
        {/* Search box with icon */}
        <div className="relative">
          <span className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-500">
            🔍
          </span>
          
          <input
            type="text"
            placeholder="Search for..."
            className="pl-9 pr-3 py-1 rounded text-black bg-white text-sm"
          />
        </div>

        <span className="cursor-pointer">🔔</span>
        <span className="cursor-pointer">👤</span>
      </div>
    </header>
  );
}
