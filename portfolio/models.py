
from django.db import models

class Profile(models.Model):
    
    name = models.CharField('氏名', max_length=100)
    # media/profileに画像を保存、個人情報はnull,blank=Trueとした
    img = models.ImageField('画像', upload_to='proflie')
    career = models.CharField('職業', max_length=50, null=True, blank=True)
    org = models.CharField('所属組織', max_length=50, null=True, blank=True)
    age = models.CharField('年齢', max_length=50, null=True, blank=True)

    twitter = models.URLField('twitterURL', null=True, blank=True)
    introduce = models.TextField('自己紹介')

    class Meta:
        verbose_name_plural = 'プロフィール'


class Description(models.Model):
    
    text = models.CharField('本文', max_length=300)

    # 外部のテーブル（class）から参照されたとき何を表示するか（これ指定しない、デフォルトはidが表示される）（管理画面で反映される）
    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'スキルの詳細文'


class Skill(models.Model):

    name = models.CharField('言語名', max_length=100)
    period = models.FloatField('期間', default=0)
    #ForeignLeyは外部のテーブル参照するときに使う,SET_NULLは参照先が消えたときNULLset
    description = models.ForeignKey(Description, on_delete=models.SET_NULL, null=True, verbose_name='説明文')

    #整数なら少数を整数表示にする
    def period_rounded(self):
        period = self.period
        if period.is_integer():
            period = int(period)
        return period

    class Meta:
        verbose_name_plural = '技術'


class Works(models.Model):

    title = models.CharField('タイトル', max_length=100)
    # upload_toのファイルは管理画面でアップロードした際に自動で追加される
    img = models.ImageField('画像', upload_to='works' )
    url = models.URLField('URL')
    date = models.DateField('公開日', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '作品集'