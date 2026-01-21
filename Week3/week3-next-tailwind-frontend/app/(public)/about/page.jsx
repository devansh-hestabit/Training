export const metadata = {
  title: "About HestaCart",
  description:
    "Learn more about HestaCart and how we help businesses manage commerce smarter.",
};

export default function AboutPage() {
  return (
    <main className="w-full min-h-screen bg-white text-gray-900">
      {/* Hero */}
      <section className="bg-gray-50 py-12">
        <div className="max-w-5xl mx-auto px-6">
          <h1 className="text-3xl md:text-4xl font-bold">
            About HestaCart
          </h1>

          <p className="mt-4 text-lg text-gray-600 max-w-3xl leading-relaxed text-justify">
            HestaCart is a smart commerce platform designed to help modern
            businesses operate more efficiently and make better decisions. It
            brings together sales management, inventory tracking, and real-time
            analytics into one powerful, easy-to-use dashboard. By simplifying
            daily operations and reducing manual work, HestaCart allows teams to
            focus on growth instead of complexity. Whether you’re running a
            small store or scaling a growing business, HestaCart provides the
            tools needed to stay organized, gain clear insights, and maintain
            full control over your operations. Our goal is to deliver a
            reliable, intuitive platform that adapts as your business evolves.
          </p>
        </div>
      </section>

      {/* Content */}
      <section className="py-14">
        <div className="max-w-5xl mx-auto px-6 space-y-12">
          {/* Mission */}
          <div>
            <h2 className="text-xl font-semibold text-gray-900">
              Our Mission
            </h2>

            <p className="mt-3 text-gray-600 leading-relaxed max-w-3xl text-justify">
              Our mission is to simplify business operations by providing tools
              that are powerful, easy to use, and scalable. We believe every
              business deserves clear insights and efficient workflows without
              complexity.
            </p>
          </div>

          {/* What We Do */}
          <div>
            <h2 className="text-xl font-semibold text-gray-900">
              What We Do
            </h2>

            <p className="mt-3 text-gray-600 leading-relaxed max-w-3xl text-justify">
              HestaCart combines analytics, inventory management, and secure
              transactions into a single platform. This allows teams to focus on
              growth while we handle the operational complexity behind the
              scenes.
            </p>
          </div>

          {/* Why HestaCart */}
          <div>
            <h2 className="text-xl font-semibold text-gray-900">
              Why HestaCart
            </h2>

            <ul className="mt-4 space-y-3 text-gray-600 list-disc list-inside max-w-3xl text-justify">
              <li>Simple and intuitive user experience</li>
              <li>Real-time business insights</li>
              <li>Secure and reliable infrastructure</li>
              <li>Designed to grow with your business</li>
            </ul>
          </div>
        </div>
      </section>
    </main>
  );
}
