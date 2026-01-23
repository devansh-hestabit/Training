"use client";

import Link from "next/link";

export default function Button({
  children,
  variant = "primary",
  onClick,
  href,
}) {
  const styles = {
    primary: "bg-blue-600 hover:bg-blue-700 text-white",
    warning: "bg-yellow-500 hover:bg-yellow-600 text-white",
    success: "bg-green-600 hover:bg-green-700 text-white",
    danger: "bg-red-600 hover:bg-red-700 text-white",
  };

  const className = `
    inline-flex items-center justify-center
    px-4 py-2.5 sm:px-5 sm:py-3
    text-sm sm:text-base font-medium
    rounded-lg transition-colors
    ${styles[variant]}
  `;

  if (href) {
    return (
      <Link href={href} className={className}>
        {children}
      </Link>
    );
  }

  return (
    <button onClick={onClick} className={className}>
      {children}
    </button>
  );
}
