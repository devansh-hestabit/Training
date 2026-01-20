"use client";

export default function Button({
  children,
  variant = "primary",
  onClick,
}) {
  const styles = {
    primary: "bg-blue-600 text-white",
    warning: "bg-yellow-500 text-white",
    success: "bg-green-600 text-white",
    danger: "bg-red-600 text-white",
  };

  return (
    <button
      onClick={onClick}
      className={`px-4 py-2 rounded text-sm font-medium ${styles[variant]}`}
    >
      {children}
    </button>
  );
}
