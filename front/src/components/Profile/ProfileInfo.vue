<template>
  <div style="position:relative">
    <div class="background-div">
      <!-- 배경 이미지 -->
      <div style="position:absolute left:0px top: 0px width:100%; height:100%; background: center center / cover no-repeat;" v-if="background_image===`${SERVER_URL}null`" :style="{ 'background-image': 'url(' + 'https://picsum.photos/600/200' + ')' }"></div>
      <div style="position:absolute left:0px top: 0px width:100%; height:100%; background: center center / cover no-repeat;" v-else :style="{ 'background-image': 'url(' + background_image + ')' }"></div>
      <!-- 프로필 사진 및 랭크 뱃지 -->
      <div id="header" style="position: relative; top:-5vw; left:10vw;">
        <div class="avatar" style="position:absolute; width:10rem; height:10rem; z-index:2;">
          <el-tooltip content="프로필을 수정하시겠습니까?" effect="dark" placement="top">
            <a data-bs-toggle="modal" data-bs-target="#profileModal" @click="initModal" style="z-index:1;">
              <img style="position:absolute" v-if="profile_image === `${SERVER_URL}null`" src='@/assets/user-account.png' alt="" class="profile-image">
              <img style="position:absolute" v-else :src="profile_image" alt="" class="profile-image">
            </a>
          </el-tooltip>
          <img style="position:absolute;top: 130px;left: 55px; border-radius: 100%; width: 3rem;" :src="rankImage" alt="" class="profile-badge">
        </div>
      </div>
      <!-- 유저 개요 및 랜덤 영화 추천 버튼 -->
      <div style="position:relative; top: 5vw; ">
        <div style="position: relative; left: 0vw; top: -6vw; font-size: 30px; text-align: center; margin-top:2rem; font-family: 'Black Han Sans', sans-serif;">{{ nickname }}님의 프로필 페이지
          <div style="position:relative;">
            <i style="font-size:2rem; " class="el-icon-video-camera-solid px-3" > 
              <span style="font-family: 'Black Han Sans', sans-serif;">
                대표 장르:</span>  <span style="font-family: 'Black Han Sans', sans-serif;">{{max_reviews_genre}}</span></i>
            <i style="font-size:2rem; " class="fas fa-plane-arrival px-3"> 
              <span style="font-family: 'Black Han Sans', sans-serif;"> 
                대표 지역:</span> <span style="font-family: 'Black Han Sans', sans-serif;">{{max_reviews_country}}</span>
              <img :src="countries_flag[max_reviews_country]" alt="">
            </i>
 
              <!-- <span style="font-family: 'Black Han Sans', sans-serif;" 
                v-for="g in max_reviews_country" :key=g.id>
                {{g}}
              <img v-html="countries_flag[g]">
              </span> -->
          </div>
          <div>
            <button class="btn btn-primary" @click.prevent="pickRandomCountry" style="font-family: 'Do Hyeon, sans-serif;">오늘 떠나볼 곳은?</button>
            <div>
              <span class="avatar">
                <el-tooltip id="departure" content="화성 갈끄니까~★♥" placement="right" :offset="-40" effect="light">
                  <i style="font-size:1.5rem;" class="fas fa-plane-departure" ><a style="cursor: pointer;" @click.prevent="getRandomMovie">{{min_random_country}}
                    <img :src="countries_flag[min_random_country]" alt=""></a></i>
                </el-tooltip>
              </span>
            </div>
          </div>
        </div>

        <!-- 유저 티어표 div 시작 -->
        <div style="position:relative; top:-3vw">

          <!-- 가장 적게 간 나라의 영화 중 랜덤하게 하나 추천! -->
          <div v-if="pickRandom" class="container" style="position:relative; top:-2vw;">
            <div class="card h-100">
              <div class="row g-0 text-white bg-dark">
                <button style="position: absolute; width: 5%;left: 95%; z-index:1;" class="btn btn-danger" @click="endRandomMovie">X</button>
                <div class="col-md-4">
                  <img :src="randomMovie.poster_path" alt="" class="img-fluid rounded-start">
                </div>
                <div class="col-md-8">
                  <div class="card-body">
                    <h1 class="card-title text-white" style="font-family: 'Black Han Sans', sans-serif';">
                      {{randomMovie.title}}
                    </h1>
                    <h2 class="card-text text-white"><b-icon icon="geo-alt" animation="cylon" font-scale="1" variant="success"></b-icon>
                      {{randomMovie.country_name}}
                    </h2>
                    <!-- overview 표시-->
                    <div class="card-text">
                      <h2 class="commu-rank text-white">평점: {{10*randomMovie.vote_avg}}%</h2>
                      <div style="font-size:20px;" class="commu-content" v-html="randomMovie.overview.substr(0,200)+'...'"></div>
                    </div>
                  </div>
                </div>                    
              </div>  
            </div>   
          </div>
          <!-- 랜덤 영화 추천 끝 -->
          <!-- 유저 랭크 현황 보여주기 -->
          <!-- 유저가 만랩이 아닐시  -->
          <div v-if="nextRankImage !== rankImage" style="position:relative; top:0.5rem;" class="d-flex justify-content-center justify-align-center">
            <!-- <div style="font-size: 2rem; font-family: 'Black Han Sans', sans-serif;">
              현재: 
            </div> -->
            <div class="avatar">
              <el-tooltip content="티어표 확인?!" effect="dark" placement="top-start" class="d-flex justify-content-center d-block" popper-class="tips">
                <a data-bs-toggle="modal" data-bs-target="#tierModal">
                  <img :src="rankImage" alt="@/assets/rank1.jpg"  style="width:50%; position:relative; top:-1vw; border:100%; border-radius: 100%;">
                </a>
              </el-tooltip>
            </div>
            <i class="d-block fas fa-long-arrow-alt-right fa-4x" style="margin: 0.5rem -30px; position:relative; top:-1vw;"></i>
            <div class="avatar">
              <el-tooltip content="티어표 확인?!" effect="dark" placement="top" class="d-block d-flex justify-content-center">
                <a data-bs-toggle="modal" data-bs-target="#tierModal">
                  <img :src="nextRankImage" alt="@/assets/rank1.jpg"  style="width:50%; position:relative; top:-1vw; border-radius: 100%;">
                </a>
              </el-tooltip>
            </div>
            <div style="position: relative;top: 2vw; left:-3vw; font-size: 2rem; font-family: 'Black Han Sans', sans-serif; "> 다음 승급까지 {{rankPoint.remain}}pt </div>

            <!-- 티어표 확인 Modal -->
            <div class="modal fade" id="tierModal" tabindex="-1" aria-labelledby="tierModalLabel" aria-hidden="true">
              <div class="modal-dialog">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title fw-bold" id="tierModalLabel">유저 리뷰점수 티어표</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <img class="img-responsive" src="@/assets/rank_tiers.png" alt="here?!">
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div>
            <el-progress :color="customColors" style="padding: 0px 5rem 0rem; font-size: 2rem;" :text-inside="true" :stroke-width="35" :percentage="rankPoint.current"></el-progress>
          </div>
          <!-- 유저 티어표 끝 -->

          <!-- 차트 보여주기 -->
          <el-tabs type="border-card" style="position:relative; margin: 3rem;">
            <el-tab-pane style=" overflow:auto; height:50vw;">
              <span slot="label"><i class="el-icon-video-camera-solid" ></i> 리뷰한 영화의 장르별 통계</span>
                <radar-chart style="width:50%; position:absolute;"
                  :dataset="genres_cnt" class="genre-radar-chart m-3"
                ></radar-chart>

                <div style="position:relative; float:right; margin-right: 10vw;">
                  <div v-for="i in genres_size" :key="i.idx">
                    <h3>{{genres_name[i]}}</h3>
                    <ul>
                      <li v-for="movie in review_movies_genre[i]" :key="movie.id">{{movie}}</li>
                    </ul>
                  </div>
                </div>
            </el-tab-pane>
            <el-tab-pane style=" overflow:auto; height:50vw;">
              <span slot="label"><i class="fas fa-globe-asia"></i> 리뷰한 영화의 나라별 통계</span>
                <radar-chart style="width:55%; position:absolute;"
                  :dataset="countries_cnt" class="country-radar-chart m-3"
                >
                </radar-chart>
                <div style="position:relative; float:right; margin-right: 10vw;">
                  <div v-for="i in countries_size" :key="i.idx">
                    <h3>{{countries_name[i]}}</h3>
                    <ul>
                      <li v-for="movie in review_movies_country[i]" :key="movie.id">{{movie}}</li>
                    </ul>
                  </div>
                </div>
            </el-tab-pane>
          </el-tabs>
      </div>
    </div>
    <div style="overflow:auto; position:relative;">
      <hr>
    <!-- 유저가 작성한 리뷰 목록 스크롤링 -->
    <!-- <div v-if="true" class="container" style="margin:0; padding:0;"> -->
      <div class="container" style="position:relative">        
        <p style="font-size: 45px; font-family: 'Black Han Sans', sans-serif; color: black;">{{nickname}}님의 전체 리뷰 목록</p>
        <div class="card h-100" v-for="(c,i) in count" :key="i.id" >
          <div class="row g-0 text-white bg-dark">
            <div style="position:absolute; width: 10%; left: 88%; top: 90%;  z-index:1; font-size: 2vw;">
              <router-link :to="{ name: 'Moviedetail', params: { movie_pk:reviews[i].movie}  }">더 보기</router-link>
            </div>
            <div class="col-md-3">
              <img :src="review_movies[i].poster_path" alt="" class="img-fluid rounded-start">
            </div>
            <div class="col-md-9">
              <div class="card-body">
                <h1 class="card-title text-white" style="font-family: 'Black Han Sans', sans-serif';">
                  {{review_movies[i].title}}
                </h1>
                <h2 class="card-text text-white d-inline"><b-icon icon="geo-alt" animation="cylon" font-scale="1" variant="success"></b-icon>
                  {{review_movies[i].country_name}} | 
                </h2>
                <h2 class="d-inline card-text text-white"><i class="el-icon-video-camera-solid"></i>
                  <span v-for="genre in review_movies[i].genre_names" :key="genre.id">
                    <span>{{genre}} | </span>
                  </span>
                </h2>
                <div class="card-text mt-3">
                  <h2 class="commu-writer text-white">리뷰 제목: {{reviews[i].title}}</h2>
                  <h3 class="commu-writedate">작성일: {{reviews[i].created_at.substr(0, 16) | dateFilter }}</h3>
                  <h3 class="commu-rank">평점: {{reviews[i].rank}}%</h3>
                  <div class="commu-content" style="font-size:20px;" v-html="reviews[i].content"></div>
                  <!-- <div class="">
                  <i class="fas fa-comment"></i>&nbsp;55
                  </div> -->
                </div>
              </div>
            </div>                           
              <!-- 리뷰 표시 끝 -->
          </div>  
        </div>   
      </div>
    <!-- </div> -->
    <!-- <li v-for="review in reviews" :key="review.id" class="list-item">{{ review.title }}</li> -->
    <p style="text-align: center; font-size: 45px;">No more!</p>
    </div>
  </div>
  <!--background-div 끝-->
    
    
    <div>
      <!-- 프로필 수정 Modal -->
      <div class="modal fade" id="profileModal" tabindex="-1" aria-labelledby="profileModalLabel" aria-hidden="true">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title fw-bold" id="profileModalLabel">프로필 수정</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <el-form
              :model="credentials"
              :rules="rules"
              ref="form"
              style="margin: 1rem;"
            >
              <el-form-item prop="nickname" label="닉네임">
                <el-input v-model="credentials.newNickname" placeholder="닉네임을 적어주세요!" prefix-icon="fas fa-user"></el-input>
              </el-form-item>
              <el-form-item prop="profile_image" label="프로필 이미지">
                <el-input
                  @change.native='getProfileImage'
                  type="file"
                  accept="image/*"
                  v-model="credentials.newProfileImage"
                  placeholder="profile_image"
                  prefix-icon="el-icon-picture-outline"
                  class="mt-2"
                ></el-input>
              </el-form-item>
              <el-form-item prop="background_image" label="배경 이미지 (입력 안할시 랜덤 배경)">
                <el-input
                  @change.native='getBackgroundImage'
                  type="file"
                  accept="image/*"
                  v-model="credentials.newBackgroundImage"
                  placeholder="background_image"
                  prefix-icon="el-icon-picture-outline"
                  class="mt-2"
                ></el-input>
              </el-form-item>
              <el-form-item>
                <el-button
                  id="profile-button"
                  type="primary"
                  native-type="submit"
                  @click.native.prevent="sendDataToServer"
                  block
                  class="mb-2"
                  data-bs-dismiss="modal"
                ><span style="color: black;">프로필 수정</span></el-button>
              </el-form-item>
            </el-form>
          </div>
        </div>
      </div>
    </div>
    <!-- 프로필 수정 모달 끝! -->

    
    



  </div>
</template>

<script>
import SERVER from '@/api/server.js'
import RadarChart from '@/components/Profile/RadarChart'
import { mapActions, mapState } from 'vuex'
import swal from 'sweetalert'
import _ from 'lodash'
import axios from 'axios'


export default {
  name: 'ProfileInfo',
  components: {
    RadarChart,
  },
  data: function () {
    return {
      username: localStorage.getItem('username'),
      max_reviews_genre: '',
      max_reviews_country: '',
      min_random_country: '',
      rankImage: '',
      nextRankImage: '',
      tiers: ['실버','에메랄드','골드','플레티넘','사파이어','마스터'],
      mytier: '',
      nextTier: '',
      rankPoint: {
        current: 0,
        remain: 0,
      },
      randomMovie: {},
      pickRandom: false,
      customColors: [
          {color: '#f56c6c', percentage: 20},
          {color: '#e6a23c', percentage: 40},
          {color: '#5cb87a', percentage: 60},
          {color: '#1989fa', percentage: 80},
          {color: '#6f7ad3', percentage: 100}
        ],
      // user_reviews: {},
      // genres_cnt: {},
      SERVER_URL: SERVER.URL,
      credentials: {
        newNickname: '',
        newProfileImage: '',
        newBackgroundImage: '',
      },
      rules: {
        newNickname: [
          {
            required: true,
            message: "닉네임을 적어주세요",
            trigger: "blur"
          },
        ],
      },
      count: 0,
      genres_name: [],
      countries_name: [],
      genres_size : 0,
      countries_size : 0,
      countries_flag : {
        '브라질' : "https://img.icons8.com/color/48/000000/brazil.png",
        '콜롬비아' : "https://img.icons8.com/color/48/000000/colombia.png",
        '멕시코' : "https://img.icons8.com/color/48/000000/mexico--v2.png",
        '라스베이거스' : "https://img.icons8.com/color/48/000000/usa.png",
        '워싱턴' : "https://img.icons8.com/color/48/000000/usa.png",
        '시카고' : "https://img.icons8.com/color/48/000000/usa.png",
        '캐나다' : "https://img.icons8.com/color/48/000000/canada.png",
        '칠레' : "https://img.icons8.com/color/48/000000/chile.png",
        '일본' : "https://img.icons8.com/color/48/000000/japan.png", 
        '홍콩' : "https://img.icons8.com/color/48/000000/hongkong-flag.png",
        '중국' : "https://img.icons8.com/color/48/000000/china.png",
        '인도' : "https://img.icons8.com/color/48/000000/india--v2.png",
        '호주' : "https://img.icons8.com/color/48/000000/australia-flag.png",
        '뉴질랜드' : "https://img.icons8.com/color/48/000000/new-zealand.png",
        '영국' : "https://img.icons8.com/color/48/000000/great-britain.png",
        '프랑스' : "https://img.icons8.com/color/48/000000/france.png",
        '이탈리아' : "https://img.icons8.com/color/48/000000/italy.png",
        '남아프리카공화국' : "https://img.icons8.com/color/48/000000/south-africa.png",
        '소말리아' : "https://img.icons8.com/color/48/000000/somalia.png",
        '모로코' : "https://img.icons8.com/color/48/000000/morocco.png",     
      }
    }
  },
  methods: {

    getRandomMovie: function () {
      const token = {'Authorization': `JWT ${this.jwtToken}`}
      axios({
        method: "get",
        url: `${SERVER.URL}/movies/${this.min_random_country}`,
        headers: token
      })
        .then( res => {
          this.randomMovie = res.data[0].fields
          this.pickRandom = true
          console.log(this.randomMovie)
        })
        .catch( err => {
          console.log(err)
        })
    },
    endRandomMovie: function () {
      this.pickRandom = false
    },
    initModal: function () {
      this.credentials.newNickname = this.nickname
      this.credentials.newProfileImage = ''
      this.credentials.newBackgroundImage = ''
    },
    getProfileImage (event) {
      this.credentials.newProfileImage = event.target.files[0] // *.jpg file로 담김
    },
    getBackgroundImage (event) {
      this.credentials.newBackgroundImage = event.target.files[0]

    },
    sendDataToServer () {
      if (this.credentials.newNickname === '') {
        swal ('닉네임을 적어주세요.', {
          dangerMode: true,
        })
      } else if (this.credentials.newProfileImage === '') {
        swal ('프로필 이미지를 넣어주세요', {
          dangerMode: true,
        })
      // 배경은 선택적으로 넣기!
      // } else if (this.credentials.newBackgroundImage === '') {
      //   swal ('배경 이미지를 넣어주세요', {
      //     dangerMode: true,
      //   })
      } else {
        const formData = new FormData()
        formData.append('nickname', this.credentials.newNickname)
        formData.append('profile_image', this.credentials.newProfileImage)
        formData.append('background_image', this.credentials.newBackgroundImage)
        formData.append('rank_point', this.rank_point)
        formData.append('username', this.username)
        this.profileUpdate(formData)
      }
    },
    ...mapActions([
      'profileUpdate',
    ]),
    countMaxReviewGenres () {
      const max_cnt = _.max(Object.values(this.genres_cnt))
      const result = _.filter(_.map(this.genres_cnt, (v,k) => {
        if (v===max_cnt) return k}))
      this.max_reviews_genre = result[0]
    },
    countMaxReviewCountries () {
      const max_cnt = _.max(Object.values(this.countries_cnt))
      const result = _.filter(_.map(this.countries_cnt, (v,k) => {
        if (v===max_cnt) return k}))
      this.max_reviews_country = result[0]
      // this.max_reviews_country.push(result[0])
    },
    pickRandomCountry () {
      const min_cnt = _.min(Object.values(this.countries_cnt))
      const result = _.filter(_.map(this.countries_cnt, (v,k) => {
        if (v===min_cnt) return k}))
      this.min_random_country = _.sample(result)
    },
    bindImageToRank () {
      const point = this.rank_point
      let step = 0
      if (point >= 500) {
        step = 6
      } else if (point < 500 && point >=400) {
        step = 5
      } else if (point < 400 && point >=300) {
        step = 4 
      } else if (point < 300 && point >= 200) {
        step = 3 
      } else if (point < 200 && point >= 100) {
        step = 2
      } else {
        step = 1
      }
      this.rankImage = require(`@/assets/rank${step}.jpg`)

      // 최대 랭크 도달
      if (step === 6) {
        this.nextRankImage = require(`@/assets/rank${step}.jpg`)
      } else {
        this.nextRankImage = require(`@/assets/rank${step+1}.jpg`)
        }

      this.myTier = this.tiers[step-1]
      if (step === 6) {
        this.nextTier = this.tiers[step-1]
      } else {
        this.nextTier = this.tiers[step]
      }
      if (this.rank_point<600) {
        this.rankPoint.current = point % 100
        this.rankPoint.remain = 100 - this.rankPoint.current
      } else {
        this.rankPoint.current = 100
        this.rankPoint.remain = 0
      }
      
    }
  },

  computed: {
    ...mapState([
      'nickname',
      'profile_image',
      'background_image',
      'rank_point',
      'userid',
      'reviews',
      'genres_cnt',
      'countries_cnt',
      'review_movies',
      'jwtToken',
      'review_movies_genre',
      'review_movies_country',
      'hover_idx',
    ]),

  },

  created () {
    this.countMaxReviewGenres()
    this.countMaxReviewCountries()
    this.bindImageToRank()
    this.genres_name = Object.keys(this.genres_cnt)
    this.countries_name = Object.keys(this.countries_cnt)
    this.genres_size = _.size(this.genres_name)
    this.countries_size = _.size(this.countries_name)
    this.count = _.size(this.reviews)
  },

  // substr 로 대체 가능
  filters: {
    dateFilter: function (value) { 
      return _.join(_.split(value, 'T'))
    }
  },




}
</script>

<style scoped>
.background-div {
  position: absolute;
  top: 0px;
  /* z-index: -1; */
  width: 100%;
  height: 20vw;
  margin-top: 87px;
  /* background-repeat: no-repeat;
  background-position: center; */
}

.avatar {
  border-radius: 100%;
  /* display: inline-block; */
  margin: 0 0 0 0;
  padding: 0.5rem;
  border: solid 1px rgba(255, 255, 255, 0.25);
  background-color: rgba(255, 255, 255, 0.075);
}
#header .avatar img {
  /* border-radius: 100%; */
  /* display: block; */
  cursor: pointer;
  transition: 0.3s;
}
.avatar img:hover {
  filter: brightness(1.2);
  transform: translateY(1.5px) rotate(-10deg);
}

#departure:hover {
  filter: brightness(1.2);
  transform: translateY(1.5px) rotate(-10deg);
}

/* .avartar img: */
@media screen and (max-width: 1280px) {
  #header {
    padding: 0 0 1em 0;
  }
}
#header {
  padding: 0 0 0 0;
}
.modal{
opacity:1;    
}
/* #header > a > img {
  width: 15%;
  height: 15%;
} */
.modal-open { 
  padding-right: 0px !important;
}

#profile-button {
  width: 100%;
  margin-top: 40px;
  padding: 14px 20px;
  border: none;
  cursor: pointer;
  width: 100%;
  transition: 0.5s;
  font-size: 16px;
  color: rgba(26, 28, 168, 0.82);
}

/* .genre-radar-chart {
    width:30%;
    height:30%;
}

.country-radar-chart {
    width:30%;
    height:30%;
} */
#radar-chart
.card-front {
  transform: rotateY(0deg);
}

.container {
  opacity: 0.9;
}
.profile-image {
  position: 'absolute';
  left: 0px;
  top: 0px;
  width: 100%;
  height: 100%;
  border-radius: 50%;
}
.profile-badge {
  position: 'absolute';
  top: 96px;
  left: 44px;
  width: 32px;
  animation: slide 1.4s ease-in-out infinite;
  cursor: pointer;
}

* {
  box-sizing: border-box;
  -webkit-font-smoothing: antialiased;
}


</style>
