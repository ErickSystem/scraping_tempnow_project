import NProgress from 'nprogress';
let _counter = 0;

export default {
  start: () => {
    if(_counter === 0) 
      NProgress.start()
    _counter++
  },
  done: () => {
    _counter--;
    if(_counter === 0)
      NProgress.done()
  }
}
