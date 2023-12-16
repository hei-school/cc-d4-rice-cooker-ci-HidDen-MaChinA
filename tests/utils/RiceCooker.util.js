import RiceCooker from '../../src/Ricecooker.js'

export function RiceCookerGenerator (broken = false, isFilled = false, content = [], isPlugedIn = false) {
  const forTesting = new RiceCooker()
  forTesting.broken = broken
  forTesting.isFiled = isFilled
  forTesting.setContent(content)
  forTesting.isPlugedIn = isPlugedIn
  return forTesting
}
