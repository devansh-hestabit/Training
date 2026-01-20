export default function Card({ title, color, children }) {
  return (
    <div className={`rounded text-white ${color}`}>
      <div className="px-4 py-3 font-semibold">{title}</div>
      <div className="px-4 py-3 bg-black/10">{children}</div>
    </div>
  );
}
