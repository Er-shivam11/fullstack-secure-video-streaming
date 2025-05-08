# Use official Node.js image from Docker Hub
FROM node:16

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json into the container
COPY package*.json /app/

# Install dependencies
RUN npm install

# Copy the rest of your app into the container
COPY . /app/

# Build the React app for production
RUN npm run build

# Expose the port that the app will run on
EXPOSE 3000

# Serve the React app with the built-in static server
CMD ["npm", "start"]
