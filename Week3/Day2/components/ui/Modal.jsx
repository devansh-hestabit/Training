"use client";

export default function Modal({ isOpen, children }) {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 bg-black/40 flex items-center justify-center px-4">
      <div
        className="bg-white rounded-lg p-4 sm:p-6
                   w-full max-w-md
                   max-h-[90vh] overflow-y-auto"
      >
        {children}
      </div>
    </div>
  );
}
