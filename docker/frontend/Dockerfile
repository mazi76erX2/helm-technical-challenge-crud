# Base image
FROM node:21-alpine

# Set working directory
WORKDIR /app

# Install dependencies
COPY package.json .
COPY yarn.lock .
RUN yarn install --frozen-lockfile

# Copy the Next.js project
COPY . /app/

# Build the Next.js app
RUN yarn build

# Expose the application port (if applicable)
EXPOSE 3000

# Start the Next.js production server
CMD ["yarn", "start"]
