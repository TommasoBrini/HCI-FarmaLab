# Build stage
FROM node:20-alpine AS build
WORKDIR /app

# Install dependencies
COPY package.json package-lock.json* yarn.lock* pnpm-lock.yaml* ./
# Prefer npm install by default; fallback to yarn/pnpm handled by lockfiles
RUN if [ -f yarn.lock ]; then yarn --frozen-lockfile --production=false; elif [ -f pnpm-lock.yaml ]; then npm install -g pnpm && pnpm install; else npm ci; fi

# Copy source and build
COPY . .
RUN npm run build

# Production stage
FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html

# Optional: copy a custom nginx config if present
# COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
