var api = {
  getTeachFileList: function (vm) {
    $.get('/edms/api/get_teach_file_list/', (data) => vm.teach_files = data)
  },
  getGradesignList: function (vm) {
    $.get('/edms/api/get_gradesign_file_list/', (data) => vm.gradesign_files = data)
  },
  getStudentList: function (vm) {
    $.get('/edms/api/get_student_list/', (data) => vm.students = data)
  },
  getTeachFileDetail: function (vm) {
    $.get('/edms/api/get_teach_file_detail/' +
      vm.teach_files[vm.tf_index].course_id + '/', (data) => vm.teach_file = data)
  },
  getGradesginFileDetail: function (vm) {
    $.get('/edms/api/get_gradesign_file_detail/' + vm.gradesign_files[vm.gf_index].graduation_thesis +
      '-' + vm.gradesign_files[vm.gf_index].student_id + '/', (data) => vm.gradesign_file = data)
  },
  createFile: function (file_type, data) {
    let api_url = '';
    if (file_type === 'tf')
      api_url = '/edms/api/create_teach_file/';
    if (file_type === 'gf')
      api_url = '/edms/api/create_gradesign_file/';
    $.ajax({
      url: api_url,
      type: 'POST',
      data: data,
      cache: false,
      processData: false,
      contentType: false
    })
  },
  createStudent: function (data) {
    $.ajax({
      url: "/edms/api/create_student/",
      type: 'POST',
      data: data,
      cache: false,
      processData: false,
      contentType: false
    })
  },
  uploadSingleFile: function (vm, file_type, file_id, file_name, data, student_id) {
    var api_url = ''
    if (file_type === 1) {
      api_url = '/edms/api/single_upload/tf/' + file_id + '/' + file_name + '/'
    }
    if (file_type === 2) {
      api_url = '/edms/api/single_upload/gf/' + file_id + '-' + student_id + '/' + file_name + '/'
    }
    $.ajax({
      url: api_url,
      type: 'POST',
      data: data,
      cache: false,
      processData: false,
      contentType: false,
    });
  }
}

var method = {

}



// app 变量为一个vue实例,包含了整个单页应用的页面逻辑控制,以及数据加载
var app = new Vue({
  delimiters: ['[[', ']]'],
  el: '#app',
  data: {
    dialog: false,
    single_upload_cache: {
      file_type: null,
      file_id: null,
      file_name: null,
      data: null,
      student_id: null,
      clear: function () {
        this.file_type = null
        this.file_id = null
        this.file_name = null
        this.data = null
        this.student_id = null
      }
    },
    header_title: '教学档案列表',
    teach_files: [],//教学档案列表
    teach_file: null,
    //教学档案页面的索引,如果为-1则为总列表状态,若为其余值,则获取teach_files[i]的数据给teach_file
    tf_index: -1,
    gradesign_files: [],
    gradesign_file: null,
    gf_index: -1,

    // 我的学生列表
    students: [],

    new_type: -1,//新建档案类型 1 教学方案,2 毕设档案,3 学生信息
    page_index: 1,

    //新建教学档案的数据,文件在外部的submit函数中上传
    teachers: '',//任课老师
    year: null,
    term: null,
    course_name: '',
    course_id: '',

    //新建毕业设计档案的数据,文件同样也在外部的submit函数中上传
    gradesign_thesis: '',//毕设题目
    gradesign_students: '',//新建毕设时选择的学生列表,考虑到几个人合作一份毕设的情况


    //新建学生档案的数据
    student_name: '',
    student_id: '',
    student_class: '',
    major: '',
    school: '',

  },
  methods: {
    open() {
      this.dialog = true
    },
    close() {
      this.dialog = false
      this.single_upload_cache.clear()
    },
    change_header_title(title, page_index) {
      this.header_title = title;
      this.page_index = page_index;
      this.tf_index = -1;
      this.gf_index = -1;
      this.new_type = -1;
    },
    //查看详情
    read_more(f, page_index) {
      if (page_index === 1) {
        this.tf_index = this.teach_files.indexOf(f);
        this.header_title = f.course_name + ' ' + f.course_id
      }
      else if (page_index === 2) {
        this.gf_index = this.gradesign_files.indexOf(f)
        this.header_title = f.graduation_thesis
      }
    },
    //新建档案
    new_file(new_type) {
      this.new_type = new_type;
    },
    //添加学生
    add_student(student) {
      if (this.gradesign_students.indexOf(student) >= 0)
        this.gradesign_students = this.gradesign_students.replace(student, '')
      else
        this.gradesign_students += student + ' '
    }
  },
  //Vue实例加载完成后需要获取数据列表
  mounted: function () {
    this.$nextTick(function () {
      api.getTeachFileList(this)
      api.getGradesignList(this)
      api.getStudentList(this)
    })
  },
  //通过对以下几个变量的观察,来控制相应的页面逻辑
  watch: {
    tf_index: function () {
      if (this.tf_index !== -1)
        api.getTeachFileDetail(this)
    },
    gf_index: function () {
      if (this.gf_index !== -1)
        api.getGradesginFileDetail(this)
    },
  }
})

// 此方法为提交教学档案的方法,上传的文件数据从app.$refs中获取
function submit_teach_file() {
  var data = new FormData()
  data.append('teachers', app.teachers)
  data.append('year', app.year)
  data.append('term', app.term)
  data.append('course_name', app.course_name)
  data.append('course_id', app.course_id)
  var file_names = [
    'teaching_syllabus',
    'teaching_plan',
    'student_score',
    'teaching_sum_up',
    'exam_paper',
    'exam_paper_answer',
    'exam_paper_analyze',
    'exam_part',
    'exam_make_up',
    'exam_make_up_answer',
    'exam_make_up_part']

  var form_files = [
    app.$refs.teaching_syllabus,
    app.$refs.teaching_plan,
    app.$refs.student_score,
    app.$refs.teaching_sum_up,
    app.$refs.exam_paper,
    app.$refs.exam_paper_answer,
    app.$refs.exam_paper_analyze,
    app.$refs.exam_part,
    app.$refs.exam_make_up,
    app.$refs.exam_make_up_answer,
    app.$refs.exam_make_up_part]

  for (i in file_names) {
    if (form_files[i].files.length > 0) {
      var teach_file = form_files[i].files[0]
      data.append(file_names[i], teach_file)
    }
  }
  api.createFile('tf', data);
}

function submit_gradesign_file() {
  var data = new FormData()
  data.append('gradesign_thesis', app.gradesign_thesis)
  data.append('students', get_id(app.gradesign_students))
  var file_names = [
    'task',
    'translation',
    'summary',
    'begin_report',
    'paper',
    'check_table',
    'task_record',
    'addition',
    'project_training']
  var form_files = [
    app.$refs.task,
    app.$refs.translation,
    app.$refs.summary,
    app.$refs.begin_report,
    app.$refs.paper,
    app.$refs.check_table,
    app.$refs.task_record,
    app.$refs.addition,
    app.$refs.project_training]

  for (i in file_names) {
    if (form_files[i].files.length > 0) {
      var gradesign_file = form_files[i].files[0]
      data.append(file_names[i], gradesign_file)
    }
  }
  api.createFile('gf', data)
}


function submit_student_info() {
  var data = new FormData()
  data.append('student_name', app.student_name)
  data.append('student_id', app.student_id)
  data.append('_class', app.student_class)
  data.append('major', app.major)
  data.append('school', app.school)
  api.createStudent(data)
}


function get_id(str) {
  var s = str.split(' ')
  for (i in s) {
    s[i] = s[i].split('-')[0]
  }
  return s.join(' ')
}

function upload_single_confirm(file_type, file_id, file_name, student_id) {
  var file_input = app.$refs.upload;
  file_input.click();
  var data = new FormData();

  file_input.addEventListener('change', function () {
    if (file_input.files.length > 0) {
      app.open()
      data.append(file_name, file_input.files[0])
      app.single_upload_cache.file_type = file_type
      app.single_upload_cache.file_id = file_id
      app.single_upload_cache.file_name = file_name
      app.single_upload_cache.student_id = student_id
      app.single_upload_cache.data = data
      setTimeout(() => app.$refs.upload_path.innerHTML = file_input.files[0].name, 500)
    }
  })
}

function upload_single() {
  api.uploadSingleFile(app, app.single_upload_cache.file_type, app.single_upload_cache.file_id,
    app.single_upload_cache.file_name, app.single_upload_cache.data, app.single_upload_cache.student_id)
  app.close()
  if (app.page_index === 1)
    setTimeout(() => api.getTeachFileDetail(app), 1000)
  if (app.page_index === 2)
    setTimeout(() => api.getGradesginFileDetail(app), 1000)

}