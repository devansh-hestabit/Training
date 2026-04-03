export default function Features({ features }) {
  return (
    <section className="bg-gray-50 py-16">
      <div className="max-w-7xl mx-auto px-6">
        <h2 className="text-3xl md:text-4xl font-bold text-center text-gray-900">
          Powerful Features
        </h2>

        <p className="mt-4 text-center text-gray-600 max-w-2xl mx-auto">
          Everything you need to run, analyze, and scale your business.
        </p>

        <div className="mt-16 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
          {features.map((feature) => (
            <div
              key={feature.title}
              className="bg-white p-8 rounded-2xl border shadow-sm
                         hover:shadow-lg hover:-translate-y-1 transition-all"
            >
              <div className="text-4xl">{feature.icon}</div>

              <h3 className="mt-4 text-lg font-semibold text-gray-900">
                {feature.title}
              </h3>

              <p className="mt-2 text-sm text-gray-600 leading-relaxed">
                {feature.description}
              </p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
