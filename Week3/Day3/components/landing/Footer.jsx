export default function Footer() {
  return (
    <footer className="bg-gray-950 text-gray-400">
      <div className="max-w-7xl mx-auto px-6 py-10">
        {/* Top */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-10">
          {/* Brand */}
          <div>
            <h3 className="text-xl font-bold text-white">
              HestaCart
            </h3>
            <p className="mt-3 text-sm leading-relaxed text-gray-400 max-w-sm">
              A smart commerce platform to manage sales, inventory, and analytics
              from one powerful dashboard.
            </p>
          </div>

          {/* Links */}
          <div>
            <h4 className="text-sm font-semibold text-white uppercase tracking-wide">
              Product
            </h4>
            <ul className="mt-4 space-y-2 text-sm">
              <li className="hover:text-white cursor-pointer transition">
                Features
              </li>
              <li className="hover:text-white cursor-pointer transition">
                Pricing
              </li>
              <li className="hover:text-white cursor-pointer transition">
                Integrations
              </li>
            </ul>
          </div>

          {/* Company */}
          <div>
            <h4 className="text-sm font-semibold text-white uppercase tracking-wide">
              Company
            </h4>
            <ul className="mt-4 space-y-2 text-sm">
              <li className="hover:text-white cursor-pointer transition">
                About
              </li>
              <li className="hover:text-white cursor-pointer transition">
                Blog
              </li>
              <li className="hover:text-white cursor-pointer transition">
                Contact
              </li>
            </ul>
          </div>
        </div>

        {/* Divider */}
        <div className="mt-12 border-t border-gray-800" />

        {/* Bottom */}
        <div className="mt-6 flex flex-col md:flex-row items-center justify-between text-xs text-gray-500">
          <p>
            © {new Date().getFullYear()} HestaCart. All rights reserved.
          </p>

          <div className="mt-4 md:mt-0 flex gap-6">
            <span className="hover:text-white cursor-pointer transition">
              Privacy
            </span>
            <span className="hover:text-white cursor-pointer transition">
              Terms
            </span>
            <span className="hover:text-white cursor-pointer transition">
              Security
            </span>
          </div>
        </div>
      </div>
    </footer>
  );
}
