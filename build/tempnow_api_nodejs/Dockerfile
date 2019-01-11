FROM node:6.5.0

ENV APP_DIR=/app
WORKDIR $APP_DIR 

COPY api ./ 

RUN npm i && npm run build

EXPOSE 3000

CMD ["npm", "start"]

