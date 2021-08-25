# DevOps-Challenge

Aplikacja Uruchomiona w AWS Elastic Beanstalk:http://flaskapp-env-1.eba-ufmvwdv3.us-east-2.elasticbeanstalk.com/

W folderze .github/workflows znajdują się:
- superlinter.yml; Skrypt CI testujący poprawność i jakość kodu, uruchamiany podczas wstawiania nowego kodu
- deploy.yml; Skrypt CD wgrywający kod źródłowy do AWS Elastic Beanstalk, w środowisko aktualnie działającego kontenera,

  Deploy.yml ma problem z uwierzytelnieniem AWS, podobno mogłbyć to błąd spowodowany przez Dependabot secrets. Po przeniesieniu Kluczy dostępu z secrets actions do dependabot secrets, problem dalej pozostał.

  Poprzednia wersja kodu Deploy.yml łączyła się z chmurą, wgrywała pliki do AWS S3, oraz deployowała pliki w środowisku AWS EB. Niestety Deploy kończył się błedem, Spowodowanym brakiem uprawnień. Dodanie uprawnień (IAM) urzytkownikowi oraz dopisanie możliwości usuwania elementów z S3 bucketa do skryptu Bucket policy, nie naprawiło błędów.


