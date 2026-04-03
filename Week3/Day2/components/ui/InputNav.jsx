export default function InputNav({ placeholder }) {
  return (
    <input
      placeholder={placeholder}
      className="pl-9 pr-3 py-2 sm:py-2.5
                 rounded-lg
                 text-sm sm:text-base
                 text-black bg-white
                 w-full
                 focus:outline-none focus:ring-2 focus:ring-blue-500"
    />
  );
}
