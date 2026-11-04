/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  transpilePackages: ["@opencut/ui"],
  experimental: {
    typedRoutes: true,
  },
};

module.exports = nextConfig;
