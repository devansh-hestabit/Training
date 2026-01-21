export default function Badge({ text }) {
  return (
    <span className="inline-flex items-center px-2.5 py-1 text-xs sm:text-sm
                     bg-gray-200 text-gray-800 rounded">
      {text}
    </span>
  );
}
