export default function Card({ title, color, children }) {
  return (
    <div className={`rounded-lg text-white ${color}`}>
      <div className="px-4 py-2.5 sm:px-5 sm:py-3 font-semibold text-sm sm:text-base">
        {title}
      </div>

      <div className="px-4 py-3 sm:px-5 sm:py-4 bg-black/10 text-sm sm:text-base">
        {children}
      </div>
    </div>
  );
}
