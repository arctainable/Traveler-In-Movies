<template>
  <div>
    <section class="content-section">
      <div class="container">
        <div class="row">
          <div class="col-md-8">
            <div class="project-content mt40">
              <form action="" id="review-form">
                <div class="review-write-title" style="height:100px;">
                  <div style="width:30%; float:left; ">
                  <div style="height:25px;"></div>
                  <span>
                    제목: <input type="text" v-model="review.title"/>
                  </span>
                  <div style="height:15px;"></div>
                  <span>
                    평점: {{sliderValue}}
                  </span>
                  </div>
                  <div style="width:10%; float:left;">
                  <div class="PostEditRate"></div>
                  </div>
                  <div class="PostEditSlider" style="position:relative;">
                    <circle-slider
                      v-model="sliderValue"
                      :side="100"
                      :min="0"
                      :max="100"
                      :step-size="1"
                      :circle-width-rel="10"
                      :progress-width-rel="10"
                      :knob-radius="10"
                    class="circle" style="margin-left:30;"></circle-slider>
                  </div>
                </div>
                <editor ref="toastuiEditor" :initialEditType="'wysiwyg'" />
              </form>
							<div class="PostEditLast">
								<div class="pull-right">
									<a class="register-btn" @click="createAction">등록 <i class="fas fa-check"></i></a>
                  <router-link class="register-btn" :to="{ name: 'Moviedetail', params: { movie_pk:movie.id } }">목록 <i class="fas fa-check"></i></router-link>
								</div>
								<div class="clearfix"></div>
							</div>
						</div>
          </div>
          <div class="col-md-4">
            <div class="writer-info mt40">
              <div class="writer-card">
                <div class="review-movie-title">{{movie.title}}</div>
                <img class="review-movie-photo" :src="movie.poster_path" >
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import Vue from 'vue'
import axios from 'axios'
import 'codemirror/lib/codemirror.css'; 
import '@toast-ui/editor/dist/toastui-editor.css'; 
import { Editor } from '@toast-ui/vue-editor';
import { mapState, mapActions} from 'vuex'
import VueCircleSlider from 'vue-circle-slider'
import Swal from 'sweetalert2'

Vue.use(VueCircleSlider)


export default {
  name: 'Moviedetail',
  components: { 
    Editor, 
  },
  data: function () {
    return {
      rankTierImage: require(`@/assets/rank_tiers.png`),
      movie: null,
      tokenHeader: null,
      review: {
        title: '',
        content: '',
        movie_id: null,
      },
      sliderValue: '',
    }
  },
  methods: {
    ...mapActions([
			// 'loginGetToken',
      'userRankpointUpdate',
      'getProfile',
      'getReviewsGenre',
      'getReviewsCountry',
      'getReviews',
      'getReviewsMovieInfo',
      'getReviewsMovieGenreCountry',
		]),
    isValid() {
      if (this.rank_point < 200 && ( this.sliderValue < 20 || this.sliderValue > 80) ) {
        Swal.fire({
            title: '<strong><u>더 강해져서 돌아오세요...?!</u></strong>',
            html: '<span style="color:red">골드 미만은 20~80점만 가능합니다!</span>',
            imageUrl: this.rankTierImage,
            imageWidth: 1400,
            imageHeight: 400,
            padding: '1em',
            imageAlt: 'Custom image',
          })
        
      } else {
        this.createAction()
      }
    },
    createAction() {
      // 유저 랭크에 따라서 리뷰 점수 가능 여부 판단
      // 유저 점수가 200점 미만인 20점 미만 80 점을 줄 수  없음
      // const ranktierImage = '@/assets/rank_tiers.png'
      
      this.review.movie_id = this.movie.id
      this.review.rank = this.sliderValue
      var content = this.$refs.toastuiEditor.invoke("getHTML");
      this.review.content = content
      // content를 저장하는 액션 처리
      // console.log(JSON.stringify(this.review))
      axios({
        // axios는 JSON.stringify를 자체적으로 해준다. 즉 data로 
        // 넘기는 값은 JSON.stringify를 해줄 필요가 없다.
        method: 'post',
        url: 'http://127.0.0.1:8000/movies/' + this.movie_pk + '/reviews/',
        headers: this.tokenHeader,
        data: this.review
      })
        .then(res => {
          console.log(res)
          this.$router.push({ name: 'Moviedetail' })
          // this.rank_point += 10
          const formData = new FormData()
          formData.append('rank_point', this.rank_point+10)
          formData.append('username', localStorage.getItem('username'))
          this.userRankpointUpdate(formData)
          this.getProfile().then((result) => {
            console.log(result)
            this.getReviewsGenre()
            this.getReviewsCountry()
            this.getReviews()
            this.getReviewsMovieInfo()
            this.getReviewsMovieGenreCountry()

          })
          
          Swal.fire({
            position: 'top-end',
            icon: 'success',
            title: 'Point +10!!',
            showConfirmButton: false,
            timer: 1500
          })
        })
        .catch(err => {
          // 에러출력
          console.log(err)
        })

    }
  },
  props: {
    movie_pk: {
      type: String,
    }
  },
  created: function () {
    let token = localStorage.getItem('jwt')
    this.tokenHeader = {}
    const currentUser = localStorage.getItem("username");
    console.log(currentUser)
    if (token) {
      this.tokenHeader['Authorization'] = `JWT ${token}`
      this.isLogin = true
    } else {
      this.isLogin = false
    }
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/movies/' + this.movie_pk,
      headers: this.tokenHeader,
    })
      .then(res => {
        console.log(res.data)
        this.movie = res.data
        this.username = currentUser
      })
      .catch(err => {
        console.log(err)
      })
  },
  computed: {
    ...mapState([
      'rank_point'
    ]),
  }
}
</script>
<style scoped>
/* .container {
  margin-top: 84px;
} */
.content-section {
  height:900px;
  background: #37373d;
}
#review-form {
  height: 84%;
}
.review-movie-title {
  text-align: center;
  font-size: 20px;
  margin-bottom: 5px;
}
.review-movie-photo {
  width:50%;
  margin-left: 25%;
  margin-right: 25%;
}
html {
  min-height: fit-content;
}
.project-content {
  height: 650px;
}
.circle {
  float:left;
  margin-left: 50px;
}
.review-write-title {
  margin-bottom: 30px;
}
</style>