export default function Testimonials({ testimonials }) {
  return (
    <section className="py-16">
      <div className="max-w-7xl mx-auto px-6">
        <h2 className="text-3xl md:text-4xl font-bold text-center text-gray-900">
          Trusted by Growing Businesses
        </h2>

        <p className="mt-4 text-center text-gray-600 max-w-2xl mx-auto">
          Teams around the world use HestaCart to simplify operations.
        </p>

        <div className="mt-16 grid grid-cols-1 md:grid-cols-3 gap-8">
          {testimonials.map((t) => (
            <div
              key={t.name}
              className="bg-white p-8 rounded-2xl border shadow-sm
                         hover:shadow-lg transition"
            >
              <p className="text-gray-700 italic leading-relaxed">
                “{t.text}”
              </p>

              <div className="mt-6">
                <div className="font-semibold text-gray-900">
                  {t.name}
                </div>
                <div className="text-sm text-gray-500">
                  {t.role}
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
