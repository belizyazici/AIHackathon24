# Ders Odam Web Uygulaması

Ders Odam, ortaokul öğrencilerinin eğitim süreçlerini desteklemek için tasarlanmış kapsamlı bir web uygulamasıdır. Uygulama, çeşitli eğitim kaynakları, etkileşimli sohbetler sunan bir chatbot ve müfredatlara uygun eğitim videoları ile öğrencilerin öğrenme deneyimlerini zenginleştirir. Hedefimiz, öğrencilerin eğitimde daha aktif rol almalarını sağlamak ve öğrenmeyi eğlenceli hale getirmektir.

![image](https://github.com/user-attachments/assets/a41fc994-33cd-4ff9-846f-bb79a4a65b91)


## İçindekiler
- [Özellikler](#özellikler)
- [Kullanılan Teknolojiler](#kullanılan-teknolojiler)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Dosya Yapısı](#dosya-yapısı)
- [API Yapılandırması](#api-yapılandırması)
- [Chatbot İşlevselliği](#chatbot)
- [Video Kaynakları](#video-kaynakları)
- [Stil](#stil)

## Özellikler
- **Etkileşimli Chatbot**: Google Generative AI tarafından desteklenen bir sohbetbotuyla etkileşime geçin ve ortaokul seviyesine göre uyarlanmış eğitimsel yanıtlar sağlayın. Bot, karmaşık konuları basitleştirir ve 8. sınıf öğrencilerine uygun bir şekilde iletişim kurar. - **Eğitim Kaynakları**: Kullanıcılar, her biri sınıfa özgü içerikler sunan Türkçe, Matematik, Fen, Yabancı Dil ve Sosyal Bilgiler gibi çeşitli konularda gezinebilir.
- **Video Oynatıcı**: Entegre video oynatıcı, öğrencilerin eğitim videolarını doğrudan platform içinde izlemelerine olanak tanır ve görsel yardımcılarla öğrenme deneyimlerini geliştirir.
- **Duyarlı Tasarım**: Uygulama, farklı cihazlarda erişilebilirliği garanti ederek mobil uyumlu olacak şekilde tasarlanmıştır.
- **Kullanıcı Dostu Gezinme**: Basit ve sezgisel gezinme yapısı, farklı konulara ve sınıflara kolay erişim sağlar.

![image](https://github.com/user-attachments/assets/61d3d1cd-6140-4110-920e-917436b29e8a)


## Kullanılan Teknolojiler
- **Flask**: Sunucu tarafı mantığı ve yönlendirme için kullanılan, Python için hafif bir web çerçevesi.
- **HTML/CSS**: Web sayfalarını yapılandırmak ve biçimlendirmek, görsel olarak çekici bir düzen sağlamak için.
- **JavaScript**: Frontend'de dinamik etkileşimler için, kullanıcı katılımını artırmak için.
- **Google Generative AI**: Chatbot işlevselliğini güçlendirmek, kullanıcı sorularına yanıt vermesini sağlamak için. - **YouTube API**: Konularla ilgili eğitim videolarını getirir ve daha geniş bir kaynak yelpazesi sunar.

## Kurulum
1. Depoyu kopyalayın:
```bash
git clone https://github.com/yourusername/ders-odam.git
cd ders-odam
```

2. Sanal bir ortam kurun (isteğe bağlı ancak önerilir):
```bash
python -m venv venv
source venv/bin/activate # Windows'ta `venv\Scripts ctivate` kullanın
```

3. Gerekli paketleri kurun:
```bash
pip install Flask google-generativeai
```

4. Ortam değişkenlerinizi kurun:
- Kök dizinde bir `.env` dosyası oluşturun ve Google API anahtarınızı ekleyin:
```plaintext
GOOGLE_API_KEY=your_api_key_here
```

## Kullanım
1. Flask uygulamasını çalıştırın:
```bash
python app.py
```

2. Web tarayıcınızı açın ve `http://127.0.0.1:5000/` adresine gidin.

3. Bir sınıf seviyesi veya konu seçmek için gezinme menüsünü kullanın. Her bölüm, o konu için ilgili içerik içerir.

4. Belirlenen giriş alanına sorularınızı yazarak sohbet robotuyla etkileşim kurun. Bot, sağlanan müfredat yönergelerine göre yanıt verecektir.

5. Her konu bölümünde bulunan konulara tıklayarak eğitim videoları izleyin. Videolar doğrudan uygulama içine yerleştirilmiştir.

## Dosya Yapısı
```
ders-odam/
├── app.py # Ana uygulama betiği
├── eduweb.js # Videoları almak ve görüntülemek için JavaScript
├── templates/ # Sayfaları işlemek için HTML dosyaları içerir
│ ├── dil.html
│ ├── fifth.html
│ ├── sixth.html
│ ├── seventh.html
│ ├── eighth.html
│ └── website.html ...
└── static/ # CSS ve resimler gibi statik dosyalar içerir
├── css/
│ ├── styledil.css # CSS için dil bölümü
│ └── style.css # Genel CSS stilleri
└── classroom.jpg... # Uygulama için resimler
```

## API Yapılandırması
- Google Generative AI özelliklerini kullanmak için, API anahtarının ortam değişkenlerinizde doğru şekilde ayarlandığından emin olun.
- Google Cloud Console'unuzda gerekli Google API'lerini (ör. Generative AI API, YouTube Data API) etkinleştirin.

## Chatbot
- Chatbot, eğitim yardımı sağlamak için tasarlanmıştır. Bir kullanıcı bir mesaj gönderdiğinde, girdi işlenir ve bot, ortaokul kitlesi için uygun bir yanıt oluşturur.
- Örnek etkileşim:
- Kullanıcı: "Matematikte çarpma işlemini anlat."
- Bot: "Çarpma işlemi, bir sayısının kendisiyle belirli sayıda toplanmasıdır..."

## Video Kaynakları
- Her konu bölümü, birimlerin bir listesini içerir ve her birimde ilgili eğitim videoları bulunur.
- Videolar doğrudan sayfadan oynatılabilir ve görsel içerikle öğrenme deneyimi geliştirilebilir. 

## Stil
- CSS dosyaları, duyarlı ve görsel olarak çekici bir tasarım oluşturmak için kullanılır. Düğmeler, başlıklar ve kapsayıcılar dahil olmak üzere farklı bölümler için stiller tanımlanır.
- Font Awesome, kullanıcı arayüzünü geliştirmek için simgeler eklemek için kullanılır.
