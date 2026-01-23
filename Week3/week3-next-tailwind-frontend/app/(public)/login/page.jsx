"use client";

import Modal from "@/components/ui/Modal";
import InputNav from "@/components/ui/InputNav";
import Button from "@/components/ui/Button";
import { User, Lock } from "lucide-react";

export default function LoginPage() {
  return (
    <Modal isOpen={true}>
      <div className="space-y-5">
        {/* Username */}
        <div className="relative">
          <User className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400 w-4 h-4" />
          <InputNav placeholder="Username" />
        </div>

        {/* Password */}
        <div className="relative">
          <Lock className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400 w-4 h-4" />
          <InputNav placeholder="Password" />
        </div>

        {/* Remember + Forgot */}
        <div className="flex items-center justify-between text-sm text-gray-500">
          <label className="flex items-center gap-2">
            <input type="checkbox" className="rounded" />
            Remember me
          </label>

          <span className="italic cursor-pointer hover:underline">
            Forgot Password?
          </span>
        </div>

        {/* Login Button */}
        <Button variant="success" href="/dashboard">
          LOGIN
        </Button>
      </div>
    </Modal>
  );
}
