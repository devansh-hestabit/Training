import PublicNavbar from "@/components/ui/PublicNavbar";

export default function PublicLayout({ children }) {
  return (
    <>
      <PublicNavbar />
      <main className="p-6 flex bg-gray-50 min-h-screen">
        {children}
      </main>
    </>
  );
}
