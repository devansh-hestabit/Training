import Image from "next/image";
import Link from "next/link";

export default function Hero() {
  return (
    <section className="max-w-7xl mx-auto px-6 py-16 grid grid-cols-1 md:grid-cols-2 gap-16 items-center">
      {/* Text */}
      <div>
        <span className="inline-block text-sm font-medium text-blue-600 bg-blue-50 px-4 py-1.5 rounded-full">
          Smart Commerce Platform
        </span>

        <h1 className="mt-6 text-4xl md:text-5xl font-bold text-gray-900 leading-tight">
          Manage your business smarter with HestaCart
        </h1>

        <p className="mt-5 text-lg text-gray-600 max-w-xl">
          HestaCart helps you manage sales, inventory, and analytics from one
          simple and powerful dashboard.
        </p>

        <div className="mt-8 flex flex-wrap gap-4">
          {/* Primary Button */}
          <Link
            href="/login"
            className="inline-flex items-center justify-center rounded-lg bg-blue-600 px-6 py-3 text-lg font-medium text-white
                       hover:bg-blue-700 transition-colors"
          >
            Get Started
          </Link>

          {/* Outline Button */}
          <button
            className="inline-flex items-center justify-center rounded-lg border border-gray-300 px-6 py-3 text-lg font-medium text-gray-700
                       hover:bg-gray-100 transition-colors"
          >
            Learn More
          </button>
        </div>

        <p className="mt-5 text-sm text-gray-500">
          No credit card required • Free 14-day trial
        </p>
      </div>

      {/* Image */}
      <div className="relative w-full h-80 md:h-105">
        <Image
          src="/hero.png"
          alt="HestaCart dashboard preview"
          fill
          priority
          className="object-contain"
        />
      </div>
    </section>
  );
}
