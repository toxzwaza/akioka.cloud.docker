FROM php:8.2-apache

# 必要なツールをインストール
RUN apt-get update && apt-get install -y \
    nano \
    git \
    unzip \
    curl \
    libzip-dev \
    libonig-dev \
    zip \
    npm \
    nodejs \
    && docker-php-ext-install pdo_mysql zip

# Composerをインストール
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Node.jsをインストール
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs

# Apacheのドキュメントルートを設定
RUN sed -i 's|DocumentRoot /var/www/html|DocumentRoot /var/www/html/laravel/public|g' /etc/apache2/sites-available/000-default.conf

# Apacheモジュールの有効化
RUN a2enmod rewrite

# 作業ディレクトリを設定
WORKDIR /var/www/html

# Laravelプロジェクトをコピー（仮定: ローカルにlaravelプロジェクトがある）
COPY ./laravel/ /var/www/html/laravel


# パーミッションの設定
RUN chown -R www-data:www-data /var/www/html && \
    chmod -R 775 /var/www/html/laravel/storage /var/www/html/laravel/bootstrap/cache

# 必要なNode.jsパッケージのインストール（仮定: Laravelプロジェクトにpackage.jsonが存在する）
WORKDIR /var/www/html/laravel

# Laravel依存関係をインストール
RUN composer install --no-dev --optimize-autoloader

RUN npm install && npm audit fix && npm run build

# 最終作業ディレクトリを公開ディレクトリに設定
WORKDIR /var/www/html
