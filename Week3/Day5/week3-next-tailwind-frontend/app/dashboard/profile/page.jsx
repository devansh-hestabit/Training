import Image from "next/image";
import Link from "next/link";

export default function ProfilePage() {
  return (
    <div className="space-y-6 text-gray-900">
      {/* Go back */}
      <Link
        href="/dashboard/"
        className="text-blue-600 text-sm hover:underline"
      >
        ← Go back
      </Link>

      {/* Profile Card */}
      <div className="bg-white border rounded-lg p-6">
        {/* Top section */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {/* Profile Image */}
          <div className="flex justify-center md:justify-start">
            <Image
              src="/profile.jpeg"
              alt="Profile"
              width={160}
              height={160}
              className="rounded-md object-cover"
            />
          </div>

          {/* User Info */}
          <div className="md:col-span-2 grid grid-cols-1 sm:grid-cols-2 gap-6 text-sm">
            <div>
              <p className="text-gray-500">Name</p>
              <p className="font-medium">Nina Valentine</p>
            </div>

            <div>
              <p className="text-gray-500">LinkedIn</p>
              <a href="#" className="text-blue-600 hover:underline">
                linkedin.com
              </a>
            </div>

            <div>
              <p className="text-gray-500">Job Title</p>
              <p className="font-medium">Actress</p>
            </div>

            <div>
              <p className="text-gray-500">Twitter</p>
              <a href="#" className="text-blue-600 hover:underline">
                www.x.com
              </a>
            </div>

            <div>
              <p className="text-gray-500">Email</p>
              <a href="#" className="text-blue-600 hover:underline">
                nina_val@example.com
              </a>
            </div>

            <div>
              <p className="text-gray-500">Facebook</p>
              <a href="#" className="text-blue-600 hover:underline">
                facebook.com
              </a>
            </div>
          </div>
        </div>

        {/* Divider */}
        <hr className="my-6" />

        {/* Bio */}
        <div className="space-y-2 text-sm text-gray-700">
          <p className="font-medium">Bio</p>
          <p>
            Nina Valentine is a creative professional with a passion for
            storytelling and digital media. With experience across multiple
            projects, she brings strong attention to detail, adaptability, and a
            collaborative mindset. She enjoys working in fast-paced environments
            and continuously learning new tools and technologies. Outside of
            work, Nina is interested in photography, travel, and exploring
            creative expression through design and performance.
          </p>
        </div>

        {/* Edit Profile */}
        <div className="mt-4">
          <Link href="#" className="text-blue-600 text-sm hover:underline">
            Edit Profile
          </Link>
        </div>
      </div>
    </div>
  );
}
