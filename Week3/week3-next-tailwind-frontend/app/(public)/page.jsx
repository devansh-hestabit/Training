import Hero from "@/components/landing/Hero";
import Features from "@/components/landing/Features";
import Testimonials from "@/components/landing/Testimonials";
import Footer from "@/components/landing/Footer";

export const metadata = {
  title: "HestaCart – Smart Commerce Platform",
  description:
    "HestaCart helps businesses manage sales, inventory, and analytics through a modern dashboard.",
};

const FEATURES = [
  {
    title: "Real-time Analytics",
    description: "Track sales and performance instantly with live insights.",
    icon: "📊",
  },
  {
    title: "Inventory Management",
    description: "Stay on top of stock levels and product movement.",
    icon: "📦",
  },
  {
    title: "Secure Payments",
    description: "Industry-grade security for every transaction.",
    icon: "🔒",
  },
  {
    title: "Custom Reports",
    description: "Generate reports tailored to your business needs.",
    icon: "📝",
  },
];

const TESTIMONIALS = [
  {
    name: "Alex Morgan",
    role: "E-commerce Founder",
    text: "HestaCart transformed how we manage sales and inventory.",
  },
  {
    name: "Priya Singh",
    role: "Operations Manager",
    text: "Beautiful UI with insights that actually help decisions.",
  },
  {
    name: "John Carter",
    role: "Retail Owner",
    text: "Exactly what a modern business platform should feel like.",
  },
];

export default function HomePage() {
  return (
    <main className="flex flex-col w-full min-h-screen bg-white text-gray-950 overflow-x-hidden">
      <Hero />
      <Features features={FEATURES} />
      <Testimonials testimonials={TESTIMONIALS} />
      <Footer />
    </main>
  );
}
