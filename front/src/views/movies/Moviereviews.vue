<template>
  <div>
		<section>
			<div class="container">
				<div class="project-head">
					<div class="head-info">
						<div class="row">
							<div class="col-md-4" style="padding-top:30px;">
                <a :href="movie.poster_path" target="_blank">
                  <img class="projectimg" :src="movie.poster_path" style="width:300px;">
                </a>
							</div>
							<div class="col-md-8">
								<div class="fundding-info" v-bind="movie">
									<div class="fundding-amount mt10">
                    <h1 class="">{{movie.title}}</h1>
                    <span class="fundding-stat"></span>
                  </div>
									<div class="mt40">
										<span class="info-text">평점</span> 
                    <br>
										<span class="info-now mr5">{{ movie.vote_avg }} / 10</span> 
                    <br>
										<span class="info-goal">{{ movie.vote_count }} Ratings</span>
									</div>
									<div class="mt20">
										<span class="info-text">줄거리</span> 
                    <br>
										<span class="info-now mr5">{{ movie.overview}}</span> 
										<br>
                    <span class="info-goal"></span>
									</div>
									<div class="mt40 btn-warp">
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</section>
		<section>
			<div class="project-bar">
			</div>
		</section>
    <section class="content-section">
      <div class="container">
        <div class="row">
          <div class="col-md-12">
            <!-- 리뷰 목록 -->
            <div id="project-content" class="project-content mt40">
              <div class="community-card">
                <div class="community-card-head">
                  <span>
                    <img class="user-photo" v-if="review.user.profile_image === `${SERVER_URL}null`" src='@/assets/user-account.png' alt="">
                    <img class="user-photo" v-else :src="review.user.profile_image" alt="">
                  </span>
                  <div class="commu-write">
                    <span class="commu-writer">제목: {{review.title}}</span><br/>
                    <span class="commu-writer">작성자: {{review.user.nickname}}</span><br/>
                    <span class="commu-writedate">작성일: {{review.created_at.substr(0,10)}} / {{review.created_at.substr(11,8)}}</span>
                    <br>
                    <span class="commu-rank">평점: {{review.rank}}%</span>

                  </div>
                </div>
                <div class="community-card-body-review">
                  <div class="commu-content" v-html="review.content">
                  </div>
                </div>
              </div>
              <div class="community-card-foot mt10">
                <i class="fas fa-comment"></i>&nbsp;{{commentlength}}
              </div>
              <div class="">
								<div class="comment-writer" v-if="isLogin">
									<div class="comment-inbox">
										<em class="comment-inbox-name">{{username}}</em>
										<textarea class="comment-inbox-text" placeholder="댓글을 남겨주세요" 
                    rows="3" cols="30" type="text" v-model="commentval"></textarea>
									</div>
									<div class="commnet-btns">
										<div class="pull-right">
											<a class="pointer comment-register" @click="createComment">등록</a>
										</div>
										<div class="clearfix"></div>
									</div>
								</div>
                <div class="comment-writer" v-else>
									<div class="comment-inbox">
										<em class="comment-inbox-name">{{username}}</em>
										<textarea class="comment-inbox-text" placeholder="로그인 후 이용 가능합니다" rows="3" cols="30" readonly></textarea>
									</div>
									<div class="commnet-btns">
										<div class="pull-right">
										</div>
										<div class="clearfix"></div>
									</div>
								</div>
							</div>
							<div><!-- 댓글창 -->
              <div class="border-bottom"></div>
								<div class="user-comment mt20" v-for="comment in comments" v-bind:key='comment.id'>
									<div class="pull-left">
                    <img class="user-photo" v-if="comment.user.profile_image === 'null'" src='@/assets/user-account.png' alt="">
                    <img class="user-photo" v-else :src="`${SERVER_URL}`+comment.user.profile_image" alt="">
									</div>
									<div class="pull-left comment-content">
										<p>{{comment.user.nickname}}</p>
										<p>{{comment.content}}</p>
									</div>
									<div class="pull-right">
										<span>{{comment.created_at.substr(0,10)}} / {{comment.created_at.substr(11,5)}}</span>
									</div>
									<div class="clearfix"></div>
									<div class="commnet-btns">
										<div class="pull-right">
											<a class="pointer comment-register" @click="deleteComment(comment)">삭제</a>
										</div>
										<div class="clearfix"></div>
									</div>
								</div>
							</div>
              <!-- 댓글창 -->
            </div>
            <div class="review-btn" v-if="review.user.username === username">
              <router-link :to="{ name: 'Moviereviewsupdate', params: { movie_pk:movie.id, username:getusernamei } }" >
                <button class="register-btn">수정하기</button>
              </router-link>
              <button class="register-btn" @click="deleted()" >삭제하기</button>
              <router-link :to="{ name: 'Moviedetail', params: { movie_pk:movie.id } }" >
                <button class="register-btn">리뷰목록</button>
              </router-link>
            </div>
            <div v-else>
              <router-link :to="{ name: 'Moviedetail', params: { movie_pk:movie.id } }" >
                <button>리뷰목록</button>
              </router-link>
            </div>
            <!--  -->
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios'
import {mapState, mapActions, mapGetters} from 'vuex'
import Swal from 'sweetalert2'
import SERVER from '@/api/server.js'

export default {
  name: 'Moviereview',
  data: function () {
    return {
      SERVER_URL: SERVER.URL,
      movie: null,
      username: '',
      review: null,
      pageall: null,
      comment: null,
      commentlength: null,
    }
  },
  props: {
    movie_pk: {
      type: Number,
    },
    review_pk: {
      type: Number,
    },
    comment_pk: {
      type: Number,
    }
  },
  methods: {
        ...mapActions([
      'userRankpointUpdate',
      'getReviewsGenre',
      'getReviewsCountry',
      'getReviews',
      'getReviewsMovieInfo',
      'getReviewsMovieGenreCountry',
		]),
    getreviews() {
      let token = localStorage.getItem('jwt')
      let tokenHeader = {}
      if (token) {
        tokenHeader['Authorization'] = `JWT ${token}`
        this.isLogin = true
      } else {
        this.isLogin = false
      }
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/reviews/' + this.review_pk + '/comments/',
        headers: tokenHeader,
      })
        .then(res => {
          console.log(res.data.length),
          this.comments = res.data
          this.commentlength = res.data.length
        })
        .catch(err => {
          console.log(err)
        })
    },
    linkGen(pageNum) {
      return pageNum === 1 ? '?' : `?page_num=${pageNum}`
    },
    deleted: function () {
      let token = localStorage.getItem('jwt')
      let tokenHeader = {}
      if (token) {
        tokenHeader['Authorization'] = `JWT ${token}`
        this.isLogin = true
      } else {
        this.isLogin = false
      }
      let url = 'http://127.0.0.1:8000/movies/' + this.movie_pk + '/reviews/' + this.review_pk +'/'
      axios({
        method: 'delete',
        url: url,
        headers: tokenHeader,
      })  
      .then(res => {
        console.log(res.data.length),
        this.review = res.data
        this.$router.push({ name: 'Moviedetail' })

        const formData = new FormData()
          formData.append('rank_point', this.rank_point-10)
          formData.append('username', localStorage.getItem('username'))
          this.userRankpointUpdate(formData)
          this.getReviewsGenre()
          this.getReviewsCountry()
          this.getReviews()
          this.getReviewsMovieInfo()
          this.getReviewsMovieGenreCountry()

          Swal.fire({
            position: 'top-end',
            icon: 'info',
            title: 'Point (-10)!!',
            showConfirmButton: false,
            timer: 1500
          })
      })
      .catch(err => {
        console.log(err)
      })
   },
  createComment: function () {
    let token = localStorage.getItem('jwt')
    let tokenHeader = {}
    if (token) {
      tokenHeader['Authorization'] = `JWT ${token}`
      this.isLogin = true
    } else {
      this.isLogin = false
    }
    const comment = {
      content: this.commentval,
      review_id: this.review.id,
    }
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/movies/reviews/' + this.review.id + '/comments/',
      headers: tokenHeader,
      data: comment,
    })
      .then(res => {
        console.log(res.data)
        this.comment=res.data
        this.commentval = ''
        this.getreviews()
      })
      .catch(err => {
        console.log(err)
      })
   },
   deleteComment: function (comment) {
    console.log(comment)
    let token = localStorage.getItem('jwt')
    let tokenHeader = {}
    if (token) {
      tokenHeader['Authorization'] = `JWT ${token}`
      this.isLogin = true
    } else {
      this.isLogin = false
    }
    axios({
      method: 'delete',
      url: 'http://127.0.0.1:8000/movies/comments/' + comment.id + '/',
      headers: tokenHeader,
    })
      .then(res => {
        console.log(res.data)
        this.getreviews()
      })
      .catch(err => {
        console.log(err)
      })
   }
  },
  created: function () {
    let token = localStorage.getItem('jwt')
    let tokenHeader = {}
    const currentUser = localStorage.getItem("username");
    console.log(currentUser)
    if (token) {
      tokenHeader['Authorization'] = `JWT ${token}`
      this.isLogin = true
    } else {
      this.isLogin = false
    }
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/movies/' + this.movie_pk,
      headers: tokenHeader, currentUser
    })
      .then(res => {
        console.log(res.data)
        this.movie = res.data
        this.username = currentUser
      })
      .catch(err => {
        console.log(err)
      })
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/movies/reviews/' + this.review_pk + '/comments/',
      headers: tokenHeader,
    })
      .then(res => {
        console.log(res.data.length),
        this.comments = res.data
        this.commentlength = res.data.length
      })
      .catch(err => {
        console.log(err)
      })
    let url = 'http://127.0.0.1:8000/movies/' + this.movie_pk + '/reviews/' + this.review_pk +'/'
    axios({
      method: 'get',
      url: url,
      headers: tokenHeader,
    })
      .then(res => {
        console.log(res.data.length),
        this.review = res.data
      })
      .catch(err => {
        console.log(err)
      })
  },
  watch: {
    $route() {
        let token = localStorage.getItem('jwt')
        let tokenHeader = {}
        if (token) {
          tokenHeader['Authorization'] = `JWT ${token}`
          this.isLogin = true
        } else {
          this.isLogin = false
        }
      let url = 'http://127.0.0.1:8000/movies/' + this.movie_pk + '/reviews/' + this.review_pk +'/'
      axios({
        method: 'get',
        url: url,
        headers: tokenHeader,
      })
        .then(res => {
          console.log(res.data.length),
          this.review = res.data
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  computed: {
    ...mapGetters([
      'getusernamei', 
    ]),
    ...mapState([
      'profile_image',
      'rank_point',
    ])
  },
}
</script>

<style scoped>
.community-card-body-review {
    min-height: 30px;
}
.comment{
  width:100%;
  height:80px;
}
.user-comment {
  padding:10px;
}
.border-bottom {
  border-bottom:1px solid #dbdbdb;
}
a {
  text-decoration: none;
  color:white;
}
.review-btn {
  margin:auto;
}
.pointer {
    background: white;
    color: black;
    padding: 5px;
    border-radius: 5px;
}
</style>