import Navbar from "@/components/ui/Navbar";
import "./globals.css";
import Sidebar from "@/components/ui/Sidebar";

export default function RootLayout({ children }) {  
  return (
    <html lang="en">
      <body>
        <Navbar />
        <div className="flex">
          <Sidebar />
          <main className="flex-1 p-6 bg-gray-100 min-h-screen">
            {children}
          </main>
        </div>
      </body>
    </html>
  );
}